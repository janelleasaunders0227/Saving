<?php

if(!isset($_SESSION))
{
    session_start();
}

include "db_conn1.php";

if (isset($_POST['uname']) && isset($_POST['password'])) {

    function validate($data){

       $data = trim($data);

       $data = stripslashes($data);

       $data = htmlspecialchars($data);

       return $data;

    }

    $uname = validate($_POST['uname']);

    $pass = validate($_POST['password']);

    if (empty($uname)) {

        header("Location: index1.php?error=User Name is required");

        exit();

    }else if(empty($pass)){

        header("Location: index1.php?error=Password is required");

        exit();

    }else{

        $sql = "SELECT * FROM users WHERE email='$uname' AND password='$pass'";

        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) === 1) {

            $row = mysqli_fetch_assoc($result);

            if ($row['email'] === $uname && $row['password'] === $pass) {

                echo "Logged in!";

                $_SESSION['email'] = $row['email'];

                $_SESSION['firstname'] = $row['firstname'];

                $_SESSION['lastname'] = $row['lastname'];

                $_SESSION['customerID'] = $row['customerID'];

                header("Location: home1.php");

                exit();

            }else{

                header("Location: index1.php?error=Incorect User name or password");

                exit();

            }

        }else{

            header("Location: index1.php?error=Incorect User name or password");

            exit();

        }

    }

}else{

    header("Location: index1.php");

    exit();

}
