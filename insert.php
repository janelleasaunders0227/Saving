<?php
$storename = $_POST['storename'];
$city = $_POST['city'];
$date = $_POST['date'];
$time = $_POST['time'];
$total = $_POST['total'];
$tax = $_POST['tax'];
$item1 = $_POST['item1'];
$item1cost = $_POST['item1cost'];
$item1category = $_POST['item1category'];

$item2 = $_POST['item2'];
$item2cost = $_POST['item2cost'];
$item2category = $_POST['item2category'];

$item3 = $_POST['item3'];
$item3cost = $_POST['item3cost'];
$item3category = $_POST['item3category'];

$item4 = $_POST['item4'];
$item4cost = $_POST['item4cost'];
$item4category = $_POST['item4category'];

$item5 = $_POST['item5'];
$item5cost = $_POST['item5cost'];
$item5category = $_POST['item5category'];
?>

if (!empty($storename) || !empty($date) || !empty($total) || !empty($item1) || !empty($item1cost)) {
    $host = "localhost"
    $dbUsername = "root";
    $dbPassword = "Brucerocks";
    $dbname = "Toothpaste";

    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);

    if (mysqli_connect_error()) {
        die('Connect Error('. mysqli_connect_error().')'.mysqli_connect_error());
    } else{
        $SELECT = "SELECT storename from register where storename = ? Limit 1";
        $INSERT = "INSERT Into register (storename, city, date, time, total, tax, item1, item1cost, item1category, item2, item2cost, item2category, item3, item3cost, item3category, item4, item4cost, item4category, item5, item5cost, item5category), value(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";

        $stmt = $conn->prepare($SELECT);
        $stmt->bind_param("s",$storename);
        $stmt->execute();
        $stmt->bind_result($storename);
        $stmt->store_result();
        $rnum = $stmt->num_rows;

        if($rum==0){
            $stmt->close();

            $stmt = $conn->prepare($INSERT);
            $stmt->bind_param("ssssii",$storename, $city, $date, $time, $total, $tax, $item1, $item1cost, $item1category, $item2, $item2cost, $item2category, $item3, $item3cost, $item3category, $item4, $item4cost, $item4category, $item5, $item5cost, $item5category);
            $stmt->execute();
            echo "New record inserted successfully";
        } else{
            echo "Someone already registered this store name";
        }
        $stmt->close();
        $conn->close();
    }

} else{
    echo "All Fields are Required";
    die();
}
