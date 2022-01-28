function drawLine(ctx, startX, startY, endX, endY){
    ctx.beginPath();
    ctx.moveTo(startX,startY);
    ctx.lineTo(endX,endY);
    ctx.stroke();
}

function drawArc(ctx, centerX, centerY, radius, startAngle, endAngle){
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, startAngle, endAngle);
    ctx.stroke();
}


function drawPieSlice(ctx,centerX, centerY, radius, startAngle, endAngle, color ){
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(centerX,centerY);
    ctx.arc(centerX, centerY, radius, startAngle, endAngle);
    ctx.closePath();
    ctx.fill();
}


function drawSquare(ctx, centerX, centerY, size, color){
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(centerX - size/2, centerY + size/2);
    ctx.lineTo(centerX + size/2, centerY + size/2);
    ctx.lineTo(centerX + size/2, centerY - size/2);
    ctx.lineTo(centerX - size/2, centerY - size/2);
    ctx.fill();
}


function getContextValue(name) {
    return Number(document.getElementById(name).innerHTML);}


var Piechart = function(options){
    this.options = options;
    this.canvas = options.canvas;
    this.ctx = this.canvas.getContext("2d");
    this.colors = options.colors;

    this.draw = function(){
        var total_value = 0;
        var color_index = 0;
        for (var categ in this.options.data){
            var val = this.options.data[categ];
            total_value += val;
        }

        var start_angle = 0;
        for (categ in this.options.data){
            val = this.options.data[categ];
            var slice_angle = 2 * Math.PI * val / total_value;

            drawPieSlice(
                this.ctx,
                this.canvas.width/2,
                this.canvas.height/2,
                Math.min(this.canvas.width/2,this.canvas.height/2),
                start_angle,
                start_angle+slice_angle,
                this.colors[color_index%this.colors.length]
            );

            start_angle += slice_angle;
            color_index++;
        }

    }
}

var genderData = {'Мужчины': getContextValue('male'), 'Женщины': getContextValue('female')};
var jobData = {'Школники': getContextValue('Sc'), 'Студенты': getContextValue('St'),
 'Преподаватели': getContextValue('T'), 'Другие': getContextValue('O')};
alert('!!');
var myCanvas = [1, 2];
var ctx = [1, 2];
var myPiechart = [1, 2];

function create_piechart(canvas_name, canvas_data, canvas_colors){
    myCanvas = document.getElementById(canvas_name);
    myCanvas.width = 300;
    myCanvas.height = 300;
    ctx = myCanvas.getContext('2d');

    myPiechart = new Piechart(
    {
        canvas:myCanvas,
        data:canvas_data,
        colors: canvas_colors
    });
    myPiechart.draw();
}


create_piechart('genderCanvas', genderData, ["#00bfff","#ff526c", "#ffff00", "#00ff00"]);
create_piechart('jobCanvas', jobData, ["#00bfff","#ff526c", "#ffff00", "#00ff00"]);





