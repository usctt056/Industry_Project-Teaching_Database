<?php 
require_once("DBConnect.php");
if(isset($_POST['Submit']))
{
  $Title = $_POST['title'];
  $F_name = $_POST['f_name'];
  $M_name = $_Post['m_name'];
  $L_name = $_POST['l_name'];
  $Address = $_POST['address'];
  $Email = $_POST['email'];
  $Phone = $_POST['phone'];
$sql = "INSERT INTO `staff` (`Title`,`F_name`,`M_name`,`L_name`,`Address`,`Email`,`Phone`) VALUES 
('$Title','$F_name','$M_name','$L_name','$Address','$Email','$Phone')";
          if(mysqli_query($conn, $sql)){
      echo "<script>alert('Successfull new teaching staff is added')</script>";
    echo "<script>window.location='home page.html';</script>";
   } 
   else{echo "Error updating record: " . mysqli_error($conn);}
}
mysqli_close($conn);
?>