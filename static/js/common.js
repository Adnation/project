function set_values() {
    jQuery.ajax({
        url: '/get-dashboard-data/',
        type: 'GET',
        dataType:'json',
        success: function(response) {

            dashboardData = response['dashboard_data']
            counters = {
                'total_questions' : 'Total Questions',
                'total_public_questions' : 'Total Public Questions',
                'total_private_questions' : 'Total Private Questions',
                'total_answers' : 'Total Answers',
                'total_users' : 'Total Users',
                'total_tenants' : 'Total Tenants'
            }
            
            $('#counters').empty();
            
            for(i=0;i<6;i++){
                $("#counters").append(
                '<li class="list-group-item justify-content-between">' + 
                counters[Object.keys(counters)[i]]+ '<span class="badge badge-default badge-pill">' +
                 dashboardData[Object.keys(counters)[i]] + '</span></li>');
            }

            $('#top_today_consumers').empty()
            for(i=0;i<6;i++){
                $("#top_today_consumers").append(
                '<li class="list-group-item justify-content-between">' + 
                dashboardData['today_consumers'][i]['api_key']+ '<span class="badge badge-default badge-pill">' +
                 dashboardData['today_consumers'][i]['counter'] + '</span></li>');
            }

            $('#top_overall_consumers').empty()
            for(i=0;i<6;i++){
                $("#top_overall_consumers").append(
                '<li class="list-group-item justify-content-between">' + 
                dashboardData['overall_consumers'][i]['api_key']+ '<span class="badge badge-default badge-pill">' +
                 dashboardData['overall_consumers'][i]['counter'] + '</span></li>');
            }
        }
    });
}

jQuery(document).ready(function() {
    set_values();
    setInterval(function() {
        set_values();
    }, 1000 * 60 * 1);
});