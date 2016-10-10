// // location.href = 'http://www.google.com'

//alert('index.js working')
document.getElementById('error_message').style.visibility = 'hidden';
function validateForm() {
//alert('validat form working')	
var zipCode = document.getElementById('index_ZipCode').value;
var city = document.getElementById('index_City').value.toLowerCase();
var state = document.getElementById('index_State').value.toLowerCase();
var state_boolean = ValidState(state);
var zipCode_boolean = ValidZip(zipCode);
var city_boolean = ValidCity(city);
if (state_boolean == false){
	document.getElementById('error_message').innerHTML ='<span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>Error in State Value. Please input one of the 50 US states';
	document.getElementById('error_message').style.visibility = 'visible';
}else if(zipCode_boolean == false){
	document.getElementById('error_message').innerHTML ='<span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>Error in Zip Value. Please input a valid 5 digit Zip Code';
	document.getElementById('error_message').style.visibility = 'visible';
}else if(city_boolean == false ){
	document.getElementById('error_message').innerHTML ='<span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>Error in City Value. Please input a valid US city';
	document.getElementById('error_message').style.visibility = 'visible';
}else{
	location.href = 'graph/'+zipCode+'/'+city+'/'+state+'/';
}



//location.href = 'graph/19010/021/41/';

}


function ValidState(sstate) {
// alert('valiate state working')
	sstates = "wa|or|ca|ak|nv|id|ut|az|hi|mt|wy" +

				"co|nm|nd|sd|ne|ks|ok|tx|mn|ia|mo" +

				"ar|la|wi|il|ms|mi|in|ky|tn|al|fl" +

				"ga|sc|nc|oh|wv|va|pa|ny|vt|me|nh" +

				"ma|ri|ct|nj|de|md|dc";

	if (sstate == ''){
		return false;
	}

	else if (sstates.indexOf(sstate.toLowerCase() + "|") > -1) {

		return true;

		}

	
	return false;
}


function ValidZip(sZip){
	//alert('valid zip working');
	if (sZip.length ==5){
		return /^\d{5}(-\d{4})?$/.test(sZip);
	}
	else {
		return false
	}
	}

function ValidCity(city) {
	
}