var checker = 0;
frappe.listview_settings['Sales Invoice'] = {
    onload: function(listview){
        console.log("Onload List view ran :D");
        var logged_user = frappe.session.user;
        console.log(logged_user);
        var todays_date = frappe.datetime.get_today();
        frappe.route_options = {
			"posting_date": [">=", todays_date]
        };
        frappe.set_route("List", "Sales Invoice",
            {
                "posting_date": [">=", todays_date]
            }
        );
        checker = 1;
    },//*/
    refresh: function(listview){
        console.log("Refresh List view ran :D");
        var todays_date = frappe.datetime.get_today();
        frappe.route_options = {
			"posting_date": [">=", todays_date]
        };
        if (checker==1){
            frappe.set_route("List", "Sales Invoice",
            {
                "posting_date": [">=", todays_date]
            }
        );
        checker = 0;
        }
    }
};
//*/
/*
frappe.ui.form.on('Sales Invoice', {
    onload: function(listview){
        console.log("Onload List view ran :D");
    },
    refresh: function(listview){
        console.log("Refresh List view ran :D");
    },
    setup: function(listview){
        console.log("Setup List view ran :D");
    } 
})
//*/