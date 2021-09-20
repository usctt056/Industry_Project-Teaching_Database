<?php
	define ('ict342-Teachingdb_Team', ’DBUSER’);
	define ('mysql-teachingDb_team', ’TEST);
	define ('DB_HOST', 'localhost');
	define ('wsp-bict11.usc.internal', ‘’DBNAME);
	$dbc = mysqli_connect (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) OR
	  	     die ('Could not connect to MySQL: ' . mysqli_connect_error() );
	function escape_data ($data) {
		if (ini_get('magic_quotes_gpc')) {
			$data = stripslashes($data);
		}
		global $dbc;
		$data = mysqli_real_escape_string($dbc,
		trim($data));
		return $data;
	} //end of function
?>