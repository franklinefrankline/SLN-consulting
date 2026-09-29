<?php
function test_input($data)
{
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

if(!empty($_POST['Name']) && !empty($_POST['Fname']) && !empty($_POST['Subject']) && !empty($_POST['Email']) && !empty($_POST['appt']) && !empty($_POST['Number']))
{
    


$name = test_input($_POST['Name']);
$fname = test_input($_POST['Fname']);
$subject = test_input($_POST['Subject']);
$email = test_input($_POST['Email']);
$time = test_input($_POST['appt']);
$number = test_input($_POST['Number']);
$service = test_input($_POST['Services']);
$text = test_input($_POST['Message']);



$msg = '

<h2> Enquiry Form </h2>

<h4><b>Name : </b>  ' . $name . ' </h4>

<h4><b>Organisation Name : </b>  ' . $fname . ' </h4>

<h4><b>Desigination : </b> ' . $subject . '</h4>

<h4><b>Email : </b> ' . $email . '</h4>

<h4><b>Number : </b> ' . $number . '</h4>

<h4><b>Right time to call : </b> ' . $time . '</h4>

<h4><b>Service : </b> ' . $service . '</h4>

<h4><b>Description : </b> ' . $text . '</h4>

';






$to = "srinivas.c@slnconsulting.co.in,schakravarthy@hotmail.com";
$subject = "Enquire";
$message = $msg;
$headers = "From:{$email} \r\n";
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";


if (mail($to, $subject, $message, $headers)) {
  echo "<script type='text/javascript'> document.location = 'index.php'; </script>";
} else {

  echo "<script type='text/javascript'> document.location = 'index.php; </script>";
}
}else{
      echo "<script type='text/javascript'> document.location = 'index.php; </script>";
}
