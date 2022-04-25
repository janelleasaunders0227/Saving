<html>
    <body>

    <?php
    $filename - $_FILES['file']['name'];

    $location - "Upload/"-.$filename;

    if( move_uploaded_file($_FILES['file']['tmp_name'],$location)){
        echo 'File Uploaded Successfully';
    } else{
        echo '<b>Error Uploading File<b>';
    }
    ?>
</body>

</html>