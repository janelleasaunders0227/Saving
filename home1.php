<?php

session_start();

if (isset($_SESSION['customerID']) && isset($_SESSION['email'])) {

 ?>

<!DOCTYPE html>

<html>

<head>

    <title>HOME</title>

    <link rel="stylesheet" type="text/css" href="style.css">

</head>

<body>

     <h1>Hello, <?php echo $_SESSION['firstname']; ?></h1>

     <a href="logout1.php">Logout</a>

</body>

</html>

<?php

}else{

     header("Location: index1.php");

     exit();

}

 ?>
