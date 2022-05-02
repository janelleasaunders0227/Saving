<?php
session_start();
include "db_conn1.php";

if(isset($_POST['uname']) && isset($_POST['password'])){

    function validate($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return data;
    }
}

$uname = validate($_POST['uname']);
$pass = validate($_POST['password']);

if(empty($uname)) {
    header("Location: index1.php?erro=User Name is Required");
    exit();
}
else if(empty($pass)) {
    header("Location: index1.php?error=Password is Required");
    exit();
}

$sql = "SELECT * FROM Toothpaste WHERE email='$uname' AND password='$pass'";

$result = mysqli_query($conn, $sql);

if(mysqli_num_rows($result) === 1) {
    $row = mysqli_fetch_assoc($result);
    if($row['email'] === $uname && $row['password'] === $pass){
        echo "Logged In!";
        $_SESSION['email'] = $row['user_name'];
        $_SESSION['firstname'] = $row['firstname'];
        $_SESSION['lastname'] = $row['lastname'];
        $_SESSION['customerID'] = $row['customerID'];
        header("Location: home1.php");
        exit();
    }
    else{
        header("Location: index1.php?error=Incorrect Username or Password");
        exit();
    }
}
else{
    header("Location: index1.php");
    exit();
}

?>
