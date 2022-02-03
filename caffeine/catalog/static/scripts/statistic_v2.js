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


function drawPieSlice(ctx, centerX, centerY, radius, startAngle, endAngle, color ){
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


function drawRectangle(ctx, startX, startY, sizeX, sizeY, color){
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(startX, startY);
    ctx.lineTo(startX, startY - sizeY);
    ctx.lineTo(startX + sizeX, startY - sizeY);
    ctx.lineTo(startX + sizeX, startY);
    ctx.fill()
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
        if (this.options.legend){
                color_index = 0;
                var legendHTML = "";
                for (categ in this.options.data){
                    legendHTML += "<div><span class='legend' style='display:inline-block;width:20px;background-color:"+this.colors[color_index++]+";'>&nbsp;</span> "+categ+"</div>";
                }
                this.options.legend.innerHTML = legendHTML;
		}
		if (this.options.doughnut){
		    this.ctx.globalCompositeOperation = 'destination-out';
		    drawPieSlice(
				this.ctx,
				this.canvas.width/2,
				this.canvas.height/2,
				this.options.doughnut * Math.min(this.canvas.width/2,this.canvas.height/2),
				0,
				2 * Math.PI,
				"#ff0000"
			);

		}

    }
}


var Barchart = function(options){
    this.options = options;
    this.canvas = options.canvas;
    this.ctx = this.canvas.getContext("2d");
    this.color = options.color;
    this.data = this.options.data;
    this.max_value = options.max_value;
    this.rect_width = options.rect_width;
    this.rect_height = options.rect_height;
    this.values_count = options.values_count;
    this.space_width = options.space_width;
    this.rect_count = Object.keys(this.data).length;
    this.left_border = options.left_border;
    this.bottom_border = options.bottom_border;



    this.draw = function(){
        var numb = 0;

        for (let i = this.values_count; i >= 0; i--) {
            drawRectangle(this.ctx, this.left_border, this.canvas.height - (-2 + this.rect_height / this.values_count * i) - this.bottom_border, this.canvas.width, 2, '#777777');

            var labelText = i;
			this.ctx.fillStyle = "#000000";
			this.ctx.font = "15px Arial";
			this.ctx.fillText(labelText, this.left_border - 15, this.canvas.height - (-2 + this.rect_height / this.values_count * i) - this.bottom_border);
        }

        for (categ in this.data){
            val = this.options.data[categ];
            drawRectangle(this.ctx, this.left_border * 1.5 + (this.space_width + this.rect_width) * numb, this.canvas.height - this.bottom_border,
                          this.rect_width, this.rect_height / this.values_count * val, this.color);


            numb++;
        }
        drawRectangle(this.ctx, this.left_border, this.canvas.height - this.bottom_border, this.canvas.width, 3, '#000000');
        drawRectangle(this.ctx, this.left_border, this.canvas.height - this.bottom_border, 3, this.canvas.height, '#000000');


    }

}


var genderData = {'Мужчины': getContextValue('male'), 'Женщины': getContextValue('female')};
var jobData = {'Школники': getContextValue('Sc'), 'Студенты': getContextValue('St'),
 'Преподаватели': getContextValue('T'), 'Другие': getContextValue('O')};

var myCanvas = 0;
var ctx = 0;
var myPiechart = 0;
var myLegend = 0;


function create_piechart(canvas_name, canvas_data, canvas_colors, canvas_legend, doughnut = 0){
    myCanvas = document.getElementById(canvas_name);
    myCanvas.width = 400;
    myCanvas.height = 350;
    ctx = myCanvas.getContext('2d');
    myLegend = document.getElementById(canvas_legend);

    myPiechart = new Piechart(
    {
        canvas:myCanvas,
        data:canvas_data,
        colors: canvas_colors,
        legend: myLegend,
        doughnut: doughnut
    });
    myPiechart.draw();
}

function create_barchart(canvas_name, canvas_data, color, max_value, rect_width, rect_height, values_count, space_width, left_border, bottom_border){
    myCanvas = document.getElementById(canvas_name);
    myCanvas.width = 600;
    myCanvas.height = 600;
    ctx = myCanvas.getContext('2d');

    myBarchart = new Barchart(
    {
        canvas:myCanvas,
        data: canvas_data,
        color: color,
        max_value: max_value,
        rect_width: rect_width,
        rect_height: rect_height,
        values_count: values_count,
        space_width: space_width,
        left_border: left_border,
        bottom_border: bottom_border
    });
    myBarchart.draw();
}

colors = ["#6c0aab","#9a3fd5", "#fddca5", "#bbc8ba"]

create_piechart('genderCanvas', genderData, colors, 'genderLegend', 0.5);
create_piechart('jobCanvas', jobData, colors, 'jobLegend', 0.5);
create_barchart('barCanvas', {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}, '#fab73d', 8, 50, 550, 8, 30, 35, 40)
