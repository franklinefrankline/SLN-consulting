<?php
/**
 * SLN Consulting - Admin Enquiry Access Dashboard & CSV Exporter
 *
 * Provides secured web access for the SLN Consulting administrator to
 * review and export customer enquiries from server-side storage.
 */

require_once __DIR__ . '/security.php';
require_once __DIR__ . '/storage.php';

sln_send_security_headers();
sln_start_session();

// Load secret key from environment or fallback default
$adminKey = getenv('SLN_ADMIN_KEY') ?: 'sln_admin_access_2026';
$providedKey = $_GET['key'] ?? ($_POST['key'] ?? ($_SESSION['sln_admin_auth'] ?? ''));

$isAuthenticated = (!empty($providedKey) && hash_equals($adminKey, $providedKey));

if ($isAuthenticated) {
    $_SESSION['sln_admin_auth'] = $adminKey;
}

// Handle Logout
if (isset($_GET['logout'])) {
    unset($_SESSION['sln_admin_auth']);
    header('Location: admin-enquiries.php');
    exit;
}

// Handle CSV Download
if ($isAuthenticated && isset($_GET['export']) && $_GET['export'] === 'csv') {
    $dir = sln_get_storage_dir();
    $csvFile = $dir . '/enquiries.csv';
    if (file_exists($csvFile)) {
        header('Content-Type: text/csv; charset=UTF-8');
        header('Content-Disposition: attachment; filename="sln-enquiries-' . date('Y-m-d') . '.csv"');
        header('Pragma: no-cache');
        header('Expires: 0');
        readfile($csvFile);
        exit;
    } else {
        die('No enquiries recorded yet.');
    }
}

$enquiries = $isAuthenticated ? sln_get_all_enquiries() : [];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SLN Consulting — Admin Enquiry Dashboard</title>
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/css/font-awesome.min.css" rel="stylesheet">
    <style>
        body { background-color: #f1f5f9; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #1e293b; padding: 30px 15px; }
        .dashboard-card { background: #ffffff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); padding: 25px; margin-bottom: 25px; }
        .header-bar { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 15px; margin-bottom: 20px; }
        .stat-box { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 15px; text-align: center; }
        .stat-num { font-size: 26px; font-weight: 700; color: #013df5; }
        .stat-label { font-size: 13px; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; }
        .badge-contact { background: #dbeafe; color: #1e40af; }
        .badge-callback { background: #fef3c7; color: #92400e; }
        .badge-sent { background: #d1fae5; color: #065f46; }
        .badge-failed { background: #fee2e2; color: #991b1b; }
        .badge-unconf { background: #e2e8f0; color: #475569; }
        table { font-size: 13.5px; }
        th { background: #f8fafc; font-weight: 600; color: #475569; }
    </style>
</head>
<body>
<div class="container-fluid" style="max-width: 1200px;">
    <?php if (!$isAuthenticated): ?>
        <div class="row justify-content-center" style="margin-top: 80px;">
            <div class="col-md-5">
                <div class="dashboard-card text-center">
                    <h3 style="color: #013df5; margin-bottom: 20px; font-weight: 700;">SLN Consulting</h3>
                    <p class="text-muted">Admin Enquiry Access Portal</p>
                    <form method="POST" action="admin-enquiries.php">
                        <div class="form-group mb-3 text-start">
                            <label class="form-label font-weight-bold">Admin Secret Key</label>
                            <input type="password" name="key" class="form-control" placeholder="Enter admin access key" required autofocus>
                        </div>
                        <button type="submit" class="btn btn-primary w-100" style="background: #013df5; border: none; padding: 10px;">Access Enquiries</button>
                    </form>
                </div>
            </div>
        </div>
    <?php else: ?>
        <div class="dashboard-card">
            <div class="header-bar">
                <div>
                    <h2 style="color: #013df5; margin: 0; font-weight: 700;">SLN Consulting — Enquiries</h2>
                    <p class="text-muted" style="margin: 4px 0 0 0;">Server-side storage record management</p>
                </div>
                <div>
                    <a href="admin-enquiries.php?export=csv" class="btn btn-success me-2" style="font-weight: 600;">
                        <i class="fa fa-download"></i> Export CSV
                    </a>
                    <a href="admin-enquiries.php?logout=1" class="btn btn-outline-secondary">Logout</a>
                </div>
            </div>

            <!-- Stats -->
            <div class="row mb-4">
                <div class="col-md-3">
                    <div class="stat-box">
                        <div class="stat-num"><?php echo count($enquiries); ?></div>
                        <div class="stat-label">Total Enquiries</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="stat-box">
                        <div class="stat-num"><?php echo count(array_filter($enquiries, fn($e) => ($e['form_type'] ?? '') === 'contact_enquiry')); ?></div>
                        <div class="stat-label">Contact Enquiries</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="stat-box">
                        <div class="stat-num"><?php echo count(array_filter($enquiries, fn($e) => ($e['form_type'] ?? '') === 'callback_enquiry')); ?></div>
                        <div class="stat-label">Callback Requests</div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="stat-box">
                        <div class="stat-num"><?php echo count(array_filter($enquiries, fn($e) => ($e['email_status'] ?? '') === 'sent')); ?></div>
                        <div class="stat-label">Emails Dispatched</div>
                    </div>
                </div>
            </div>

            <!-- Table -->
            <div class="table-responsive">
                <table class="table table-bordered table-hover align-middle">
                    <thead>
                        <tr>
                            <th>Ref ID</th>
                            <th>Date / Time</th>
                            <th>Type</th>
                            <th>Contact</th>
                            <th>Organisation / Role</th>
                            <th>Service / Call Time</th>
                            <th>Message</th>
                            <th>Email Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php if (empty($enquiries)): ?>
                            <tr><td colspan="8" class="text-center text-muted py-4">No enquiries submitted yet.</td></tr>
                        <?php else: ?>
                            <?php foreach (array_reverse($enquiries) as $item): ?>
                                <tr>
                                    <td><code><?php echo htmlspecialchars($item['id'] ?? ''); ?></code></td>
                                    <td><small><?php echo htmlspecialchars($item['date'] ?? $item['timestamp'] ?? ''); ?></small></td>
                                    <td>
                                        <span class="badge <?php echo ($item['form_type'] ?? '') === 'callback_enquiry' ? 'badge-callback' : 'badge-contact'; ?>">
                                            <?php echo htmlspecialchars($item['form_type'] ?? 'General'); ?>
                                        </span>
                                    </td>
                                    <td>
                                        <strong><?php echo htmlspecialchars($item['name'] ?? ''); ?></strong><br>
                                        <a href="mailto:<?php echo htmlspecialchars($item['email'] ?? ''); ?>"><?php echo htmlspecialchars($item['email'] ?? ''); ?></a><br>
                                        <small><a href="tel:<?php echo htmlspecialchars($item['phone'] ?? ''); ?>"><?php echo htmlspecialchars($item['phone'] ?? ''); ?></a></small>
                                    </td>
                                    <td>
                                        <strong><?php echo htmlspecialchars($item['organisation'] ?? ''); ?></strong><br>
                                        <small class="text-muted"><?php echo htmlspecialchars($item['designation'] ?? ''); ?></small>
                                    </td>
                                    <td>
                                        <span class="badge bg-light text-dark border"><?php echo htmlspecialchars($item['service'] ?? 'General'); ?></span>
                                        <?php if (!empty($item['right_time_to_call'])): ?>
                                            <div class="mt-1"><small><strong>Call:</strong> <?php echo htmlspecialchars($item['right_time_to_call']); ?></small></div>
                                        <?php endif; ?>
                                    </td>
                                    <td><small><?php echo nl2br(htmlspecialchars($item['message'] ?? '')); ?></small></td>
                                    <td>
                                        <?php 
                                            $st = $item['email_status'] ?? 'pending';
                                            $badgeClass = ($st === 'sent') ? 'badge-sent' : (($st === 'failed') ? 'badge-failed' : 'badge-unconf');
                                        ?>
                                        <span class="badge <?php echo $badgeClass; ?>"><?php echo htmlspecialchars($st); ?></span>
                                    </td>
                                </tr>
                            <?php endforeach; ?>
                        <?php endif; ?>
                    </tbody>
                </table>
            </div>
        </div>
    <?php endif; ?>
</div>
</body>
</html>
