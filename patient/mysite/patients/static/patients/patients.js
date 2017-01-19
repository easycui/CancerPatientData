$(function() {
    $("#button1").click( function(event) {
        alert($("#123").val());
    });
    $("#submit").click(function(e){
        var dt = $('#example').dataTable().api();
        $.get('filter',$("#form_filter").serialize(),function(data){
            dt.clear();
            var obj=JSON.parse(data)
            dt.rows.add(obj.data);
            dt.draw();
            $("#number").html(obj.number)
        });
    });
    $("#ADD").click(function(e)
    {
        $.ajax({
            url:"AddNewPatient\\",
            type:"POST",
            data:$("#form_new").serialize(),
            success:function()
            {
                var dt = $('#example').dataTable().api();
                $.get('filter',function(data){
                    dt.clear();
                    var obj=JSON.parse(data)
                    dt.rows.add(obj.data);
                    dt.draw();
                    $("#number").html(obj.number)
                })
                $.getJSON('GetChart',function(data){
                var charts=["PSAChart","ProstateChart","LesionChart","SectorChart","PiradsChart","GLEASONChart"];
                var name=["PSA","prostate_vol","lesion_size","sector","PIRADS_score","GLEASON_score"];
                var i;
                for (i=0;i<name.length;i++)
                {
                    drawChart(charts[i],name[i],data[i])
                }
            });
            }
        });
    });
    $('#example').DataTable({
        "pageLength":15,
        ajax:{
            url:'loadData',
            data:'data'
        },
        columns:[
            {data:"patient_ID"},
            {data:"PSA"},
            {data:"prostate_vol"},
            {data:"lesion_size"},
            {data:"sector"},
            {data:"PIRADS_score"},
            {data:"GLEASON_score"}
        ]
    });

    $.getJSON('GetChart',function(data){

        var charts=["PSAChart","ProstateChart","LesionChart","SectorChart","PiradsChart","GLEASONChart"];
        var name=["PSA","prostate_vol","lesion_size","sector","PIRADS_score","GLEASON_score"];
        var i;
        for (i=0;i<name.length;i++)
        {
            drawChart(charts[i],name[i],data[i])
        }
    });
    function drawChart(id,name,data){
        var dataPoints = [];
        $.each(data, function(key, value){
            dataPoints.push({x: value[0], y: parseInt(value[1])});
        });
        var chart=new CanvasJS.Chart(id,
        {
            title:{
                text:"The histogram of "+name
            },
            data:[{
                type:"column",
                dataPoints:dataPoints,
            }]
        });
        chart.render();
    }
} );
