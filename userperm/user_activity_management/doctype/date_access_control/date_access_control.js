// Copyright (c) 2019, Havenir and contributors
// For license information, please see license.txt

frappe.ui.form.on('Date Access Control', {
	/*
	refresh: function(frm) {
		console.log(frm.doc.name);
	},
	//*/
	time_period_templates: function(frm){
		if (frm.doc.time_period_templates == "15 Days"){
			frm.set_value("number_of_days",15);
		}
		else if (frm.doc.time_period_templates == "30 Days"){
			frm.set_value("number_of_days",30);
		}
		else if (frm.doc.time_period_templates == "45 Days"){
			frm.set_value("number_of_days",45);
		}
		else if (frm.doc.time_period_templates == "3 Months"){
			var days_temp = 3*30;
			frm.set_value("number_of_days",days_temp);
		}
		else if (frm.doc.time_period_templates == "6 Months"){
			var days_temp = 6*30;
			frm.set_value("number_of_days",days_temp);
		}
		else if (frm.doc.time_period_templates == "1 Year"){
			var days_temp = 1*365;
			frm.set_value("number_of_days",days_temp);
		}
		else if (frm.doc.time_period_templates == "2 Years"){
			var days_temp = 2*365;
			frm.set_value("number_of_days",days_temp);
		}
		else if (frm.doc.time_period_templates == "5 Years"){
			var days_temp = 5*365;
			frm.set_value("number_of_days",days_temp);
		}
		else if (frm.doc.time_period_templates == "10 Years"){
			var days_temp = 10*365;
			frm.set_value("number_of_days",days_temp);
		}
	}
});
