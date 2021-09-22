<!DOCTYPE html>
<html>

<!-- Testing Navigator-->
<style>
    .container {
      position: relative;
    }
    
    .topleft {
      position: absolute;
      top: 0px;
      left: 0px;
      font-size: 18px;
    }
    
    </style>
    </head>
    <body>
    
    <div class="container">
      
      <div class="topleft"><a href="Home Page.html"> Home Page </a>> <a href="Teaching Staff Portal.html">Teaching Staff Portal </a>> New Teaching Staff</div>
    </div>
<!-- Background -->

<!-- Title -->
<head>
<title>Home Page</title>
</head>
<body>
<center><img src="TeachOrg Logo.png"/></center>
<center><img src="New_Teaching_Staff_Title.png"/></center>
<!-- Buttons -->
<center><h1>1. Title and name</h1>
  <form action="/action_page.php"> <!-- This is where the php file location will go-->
    <table> 
      <!-- Title -->
    <label for="title">Title:</label><br>
      <input type="text" id="title" name="title" placeholder="Mr / Mrs / Ms"><br>
      <!-- Names and stuff -->
      <label for="f_name">First Name(s):</label><br>
      <input type="text" id="f_name" name="f_name" placeholder="First Name(s)"><br>
      <label for="l_name">Last Name:</label><br>
      <input type="text" id="l_name" name="l_name" placeholder="Last Name"><br>
      <label for="address">Address:</label><br>
      <input type="text" id="address" name="address" placeholder="Address"><br>
      <label for="email">Email:</label><br>
      <input type="text" id="email" name="email" placeholder="Email Address"><br>
      <label for="phone">Phone:</label><br>
      <input type="text" id="phone" name="phone" placeholder="Phone"><br><br>
      <!-- 2 Completed Academic Qualifications -->
      <h1>2. Completed Academic Qualifications </h1>
      <label for="fname">Full name of award:</label><br>
      <input type="text" id="lname" name="lname" placeholder="Award"><br>
      <label for="fname">Subject/major area:</label><br>
      <input type="text" id="lname" name="lname" placeholder="Subject/major"><br>
      <label for="fname">Full name of awarding institution and year of award (if an overseas institution, also include the country and verification of legitimacy of the award and institution):</label><br>
      <input type="text" id="lname" name="lname" placeholder="Institution and year"><br><br>
      
      <!-- 3 Teaching experience (previous seven years)-->
      <h1>3. Teaching experience (previous seven years)</h1>
      <label for="fname">Teaching Period (from most recent):</label><br>
      <input type="text" id="lname" name="lname" placeholder="Teaching Period"><br>
      <label for="fname">Field of study area/course title:</label><br>
      <input type="text" id="lname" name="lname" placeholder="Field"><br>
      <label for="fname">Name of organisation/institution and, if an overseas instidution, the country:</label><br>
      <input type="text" id="lname" name="lname" placeholder="Organisation"><br>
      <label for="fname">Role - Course coordinator, lecturer, tutor, instructor, teaching assistant, marker, facilitator:</label><br>
      <input type="text" id="lname" name="lname" placeholder="Role"><br>
      
      
      <br>
      <!-- 4 Relevant employment/experience  -->
      <h1>4. Relevant employment/experience</h1>
      <label for="fname">Employment Period:</label><br>
      <input type="text" id="lname" name="lname" placeholder="Employmnt Period"><br>
      <label for="fname">FTE (full-time/part-time/casual):</label><br>
      <input type="text" id="lname" name="lname" placeholder="FTE"><br>
      <label for="fname">Name of employer:</label><br>
      <input type="text" id="lname" name="lname" placeholder="Employer"><br>
      <label for="fname">Position title:</label><br>
      <input type="text" id="lname" name="lname" placeholder="Title"><br>
      <label for="fname">Relevant duties:</label><br>
      <input type="text" id="lname" name="lname" placeholder="Duties"><br><br>

      <!-- 5. Other relevant information (including professional and/or honorary memberships, directorships and related scholarly activities) -->
      <h1>5. Other relevant information (including professional and/or honorary memberships, directorships and related scholarly activities)</h1>
      <label for="fname"> </label><br>
      <input type="text" id="lname" name="lname" placeholder="Enter text here"><br><br>

      <!-- 6. Publications (scholarship and research outputs)  -->
      <h1>6. Publications (scholarship and research outputs) </h1>

      
      <br>
      <!-- Submit Button -->
      <input type="submit" value="Submit">
      
      </table>
    </form> 
    

</center>

<!-- Back Button -->
<div style="
height:100%;
width:100%;">

<a href="Teaching Staff Portal.html"><img src="Back.png"
style="position:absolute;
float:left;
left:0px;
bottom:0px;
z-index:2;">
</a>
</div>




</body>
</html>