<?php
	$string = curl("http://dev.virtualearth.net/REST/v1/Traffic/Incidents/37,-105,45,-94?key=AtAWrDwvf9v0p3Ymboe3IigmSoTcWJo2T3ny75RNaCGoAkmvuj6YG01LdpqotWTY");

	$data = json_decode($string);

	echo var_dump($data);

	echo $data->severity;

?>