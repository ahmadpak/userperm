frappe.ui.form.on("Purchase Receipt", {
    refresh: function(frm,cdt,cdn){
        var doc_loading = frappe.get_doc(cdt,cdn);
        var doc_date    = doc_loading.posting_date;
        var todays_date = frappe.datetime.get_today();
        var dif_in_days = frappe.datetime.get_day_diff(todays_date,doc_date);
        var logged_user = frappe.session.user;
        if (logged_user != "Administrator"){
            frm.call({
                method: "frappe.client.get_list",
                args: {
                        doctype:    "Date Access Control",
                        filters: [
                                    ["user","=",logged_user]
                        ],
                        fields: ["number_of_days"]

                },
                callback(r){
                    if(r){
                        var userperm_list = r.message;
                        if (userperm_list[0]!= undefined){
                            var newdate     = frappe.datetime.add_days(todays_date,-1*userperm_list[0].number_of_days);
                            if(dif_in_days>userperm_list[0].number_of_days){
                                frappe.set_route("List", "Purchase Receipt",
                                    {
                                        "posting_date": [">=", newdate]
                                    }
                                );
                                frappe.msgprint("You are not allowed to view this document");    
                            }
                        }
                    }
                }
            })
        }
    },

    posting_date: function(frm,cdt,cdn){
        var current_doc = frappe.get_doc(cdt,cdn);
        var doc_date    = current_doc.posting_date;
        var todays_date = frappe.datetime.get_today();
        var dif_in_days = frappe.datetime.get_day_diff(todays_date,doc_date);
        var logged_user = frappe.session.user;
        if (logged_user != "Administrator"){
            frm.call({
                method: "frappe.client.get",
                args:   {
                            doctype:    "Date Access Control",
                            name:       logged_user
                        },
                        callback(r){
                            console.log("posting date ran");
                            var dac = r.message;
                            if(dif_in_days>dac.number_of_days){
                                frm.set_value("posting_date", todays_date);
                                frappe.msgprint("You have entered incorrect date");    
                            }
                        }
            })
        }
    }
})