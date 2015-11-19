var CGI="cgi-bin/vpn.py"

function updateCurrentVPN() {
	$("#currentSpinner").show();
	$("#currentVPN").hide();
	$.get( CGI, { request : "getCurrent" } )
			.done( function(data) {
					$("#currentSpinner").hide();
					$("#currentVPN").text(data.vpn);
					$("#currentVPN").show();
			});
}

function updateVPNList() {
	$.get( CGI, { request : "list" } )
			.done( function(data) {
					var $vpnSelect = $("#vpnSelect");
					var options = '';
					for (i=0; i < data.vpns.length; i++) {
						options += "<option>" + data.vpns[i] + "</option>";
					}
					$vpnSelect.empty().append(options);
			});
}

function setVPN() {
	var vpnName = $('#vpnSelect').find(":selected").text();
	console.log("setVpn: " + vpnName);
	$("#coutput").hide();
	$("#outputSpinner").show();
	$.get( CGI, { request : "setVpn", vpn : vpnName } )
			.done ( function(data) {
					console.log("data:" + data);
					$("#coutput").text(data.result);
					updateCurrentVPN();
					$("#coutput").show();
					$("#outputSpinner").hide();
			});
}

$(document).ready(function(){
	$("#outputSpinner").hide();
	updateCurrentVPN();
	updateVPNList();
});
