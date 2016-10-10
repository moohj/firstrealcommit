//variables
// alert("grapgview js started ");
var height = screen.height;
var width = screen.width;

var pop_label = pop_label.substr(1,pop_label.length-2).split(",");
// alert(pop_label);

// alert(income_label);
var income_label = income_label.substr(1,income_label.length-2).split(",");

// alert("alert business amount"+business_amount);
// alert("alert business name"+business_name);

var business_name = business_name.substr(1,business_name.length-2).split('", "');
var business_amount = business_amount.substr(6,business_amount.length-12).split("&#39;, &#39;").map(Number);

// alert("alert business amount"+business_amount);
 // alert("alert business name"+business_name);

// alert("alert business amount"+business_amount_county);


var business_name_county = business_name_county.substr(1,business_name_county.length-2).split('", "');

// alert("alert business name"+business_name_county);

var business_amount_county = business_amount_county.substr(6,business_amount_county.length-12).split("&#39;, &#39;").map(Number);


// alert("alert business amount"+business_amount_county);
// alert("alert business name"+business_name_county);

var pop_male = pop_male.substr(1,pop_male.length-2).split(",").map(Number);
// alert(pop_male)

var pop_female = pop_female.substr(1,pop_female.length-2).split(",").map(Number);
// alert(pop_female)

var income = income.substr(1,income.length-3).split(',').map(Number);
// alert(income);

var income_county = income_county.substr(1,income_county.length-3).split(',').map(Number);

var backgroundColorVar =[
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',

                'rgba(238, 210, 238, 0.2)',
                'rgba(133, 111, 200, 0.2)',
                'rgba(255, 216, 0, 0.2)',
                'rgba(60, 171, 113, 0.2)',
                'rgba(210, 105, 30, 0.2)',
                'rgba(113, 198, 113, 0.2)',

                'rgba(139, 26, 26, 0.2)',
                'rgba(113, 113, 198, 0.2)',
                'rgba(118, 228, 198, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(148, 0, 211, 0.2)',
                'rgba(135, 206, 255, 0.2)',
                

                'rgba(205, 165, 0, 0.2)',
                'rgba(0, 100, 0, 0.2)',
                'rgba(255, 99, 71, 0.2)',
                'rgba(198, 113, 113, 0.2)',
                'rgba(255, 255, 0, 0.2)',
                'rgba(25, 116, 205, 0.2)',
            ]
var borderColorVar = [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',

                'rgba(238, 210, 238, 1)',
                'rgba(133, 111, 255, 1)',
                'rgba(255, 216, 0, 1)',
                'rgba(60, 171, 113, 1)',
                'rgba(210, 105, 30, 1)',
                'rgba(113, 198, 113, 1)',

                'rgba(139, 26, 26, 1)',
                'rgba(113, 113, 198, 1)',
                'rgba(118, 228, 198, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(148, 0, 211, 1)',
                'rgba(135, 206, 255, 1)',
                

                'rgba(205, 165, 0, 1)',
                'rgba(0, 100, 0, 1)',
                'rgba(255, 99, 71, 1)',
                'rgba(198, 113, 113, 1)',
                'rgba(255, 255, 0, 1)',
                'rgba(25, 116, 205, 1)',
            ]

//Zipcode data
//Zipcode data
//Zipcode data
// alert("before 1st graph");
// POPulation zip
var popvar = document.getElementById("pop_can");
popvar.height = 200;
var myChart = new Chart(popvar, {
    type: 'bar',
    data: {
        labels: pop_label,
        datasets: [{
            label: 'Male Population',
            data: pop_male,
            backgroundColor:backgroundColorVar,
            borderColor:borderColorVar,
            borderWidth: 1
        },

        {
            label: 'Female Population',
            data: pop_female,
            backgroundColor:backgroundColorVar,
            borderColor:borderColorVar,
            borderWidth: 1
        },]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});


// alert('first graph completed');


// income zip
var incomevar = document.getElementById("income_can");
incomevar.height = 200;
var myChart1 = new Chart(incomevar, {
    type: 'bar',
    data: {
        labels: income_label,
        datasets: [{
            label: 'Income',
            data: income,
            backgroundColor:backgroundColorVar,
            borderColor:borderColorVar,
            borderWidth: 1
        },]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
// jobs zip
// jobs zip
// jobs zip

// alert(" working to here");

var jobsvar = document.getElementById("jobs_can");
jobsvar.height = 200;
var myChart2 = new Chart(jobsvar, {
    type: 'pie',
    data: {
        labels: business_name ,
        datasets: [{
            label: 'Jobs',
            data: business_amount,
            backgroundColor:backgroundColorVar,
            borderColor:borderColorVar,
            borderWidth: 1
        },]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});

// alert("working to here");
// //county Data
// //county Data
// //county Data

var pop_male_county = pop_male_county.substr(1,pop_male_county.length-2).split(",").map(Number);

var pop_female_county = pop_female_county.substr(1,pop_female_county.length-2).split(",").map(Number);




// POPulation bar chart
var popvar_county = document.getElementById("pop_can_county");
popvar_county.height = 200;
var myChart = new Chart(popvar_county, {
    type: 'bar',
    data: {
        labels: pop_label,
        datasets: [{
            label: 'Male Population',
            data: pop_male_county,
            backgroundColor:backgroundColorVar,
            borderColor:borderColorVar,
            borderWidth: 1
        },

        {
            label: 'Female Population',
            data: pop_female_county,
            backgroundColor:backgroundColorVar,
            borderColor:borderColorVar,
            borderWidth: 1
        },]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});

// //population pie chart


// income bar chart




var incomevar_county = document.getElementById("income_can_county");
incomevar_county.height = 200;
var myChart1 = new Chart(incomevar_county, {
    type: 'bar',
    data: {
        labels: income_label,
        datasets: [{
            label: 'Income',
            data: income_county,
            backgroundColor:backgroundColorVar,
            borderColor:borderColorVar,
            borderWidth: 1
        },]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});

var jobsvar_county = document.getElementById("jobs_can_county");
jobsvar_county.height = 200;
var myChart2 = new Chart(jobsvar_county, {
    type: 'pie',
    data: {
        labels: business_name_county ,
        datasets: [{
            label: 'Jobs',
            data: business_amount_county,
            backgroundColor:backgroundColorVar,
            borderColor:borderColorVar,
            borderWidth: 1
        },]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
