var drawPath = function(ctx, path) {
	if(path.length){
		ctx.beginPath();
		ctx.moveTo(path[0][0], path[0][1]);

		for (var i = 0 ; i < path.length; i++) {
			ctx.lineTo(path[i][0], path[i][1]);
		}
		ctx.lineWidth = 2;
		ctx.strokeStyle = 'blue';
		ctx.stroke();
		
		ctx.fillStyle = '#ff0000';
		for(var i = 0; i < path.length; i++){
			ctx.fillRect(path[i][0]-2, path[i][1]-2, 4, 4);
		}
	}
};

var getMousePos = function(canvas, evt) {
	var rect = canvas.getBoundingClientRect();
	return {
    	x: parseInt((evt.clientX - rect.left) / (rect.right - rect.left) * canvas.width),
    	y: parseInt((evt.clientY - rect.top) / (rect.bottom - rect.top) * canvas.height)
	};
}

var lineFollower = function(canvas, path, pt){
	if(canvas.getContext){
		var ctx = canvas.getContext('2d');
		ctx.clearRect(0,0,canvas.width, canvas.height);
		drawPath(ctx, path);
		ctx.beginPath();
		// use default comp. mode
		ctx.globalCompositeOperation = "source-over";
		var len = path.length;
		ctx.moveTo(path[len-1][0], path[len-1][1]);
		ctx.lineTo(pt[0], pt[1]);
		ctx.lineJoin = ctx.lineCap = 'round';
		ctx.lineWidth = 2;
		ctx.strokeStyle = 'blue';
		ctx.stroke();
	}
}

var mouseXY = function(evt, canvas, curve){
	var pos = getMousePos(canvas, evt);
	var path = curve.path();

	if(curve.follower()){
		lineFollower(curve.getCanvas(), path, [pos.x, pos.y]);
	}
}

var mouseDown = function(evt, canvas, curve){
	if(evt.buttons == 1){
		curve.setFollower(true);
		var pos = getMousePos(canvas, evt);
		curve.append([pos.x, pos.y]);
		var ctx = canvas.getContext('2d');
		var path = curve.path();
		drawPath(ctx, curve.path());
		ctx.restore();
	}else if(evt.buttons == 2){
		curve.setFollower(false);
		curve.setCurrentPath(curve.currentPath()+1);
		if(canvas.getContext){
			var ctx = canvas.getContext('2d');
			var path = curve.path();
			var len = path.length;

			ctx.clearRect(0,0,canvas.width, canvas.height);
			drawPath(ctx, path);
			
			ctx.moveTo(path[0][0], path[0][1]);
			ctx.lineTo(path[len-1][0], path[len-1][1]);
			ctx.lineWidth=2;
			ctx.strokeStyle='blue';
			ctx.fill();
			ctx.stroke();
		}
	}
}

var drawCanvas = function(obj) {
	var objs = obj.children;
	var img_div = objs[0];
	var img = img_div.children[0];
	console.log(img);
	var width = img_div.clientWidth;
	var height = img_div.clientHeight;

	var canvas = document.createElement('canvas');
	canvas.id = 'img_canvas';
	canvas.width = width;
	canvas.height = height;
	canvas.style.position = 'absolute';
	canvas.style.left = 0;
	canvas.style.top = 0;
	img_div.appendChild(canvas);	

	var ctx = canvas.getContext("2d");
	ctx.globalAlpha = 0.7;

	var curve = new Curve();
	curve.setCanvas(canvas);
	
	canvas.addEventListener("mousedown",  function(evt){
			evt.preventDefault();
			evt.stopPropagation();
			document.addEventListener('contextmenu', event => event.preventDefault());
			mouseDown(evt, this, curve);
		}, false
	);

    canvas.addEventListener("mousemove", function(evt) {
    	mouseXY(evt, this, curve);
    	}, false
    );
};


//https://jsfiddle.net/z2ngg62k/8/
