<?php
session_start();
include "db_conn.php";

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
    header("Location: index.php?erro=User Name is Required");
    exit();
}
else if(empty($pass)) {
    header("Location: index.php?error=Password is Required");
    exit();
}

$sql = "SELECT * FROM Toothpaste WHERE email='$uname' AND password='$pass'";

$result = mysqli_query($conn, $sql);

if(mysqli_num_rows($result) === 1) {
    $row = mysqli_fetch_assoc($result);
    if($row['email'] === $uname && $row['password'] === $pass){
        echo "Logged In!";
        $_SESSION['email'] = $row['user_name'];
        $_SESSION['name'] = $row['name'];
        $_SESSION['id'] = $row['id'];
        header("Location: home.php");
        exit();
    }
    else{
        header("Location: index.php?error=Incorrect Username or Password");
        exit();
    }
} 
else{
    header("Location: index.php");
    exit();
}

?>