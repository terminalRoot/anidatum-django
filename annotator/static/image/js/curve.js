var Curve = function(){
	this._path = new Object();
	this._current_path = 0;
	this._canvas = null;
	this._follower = false;
};


Curve.prototype.setCurrentPath = function(cp){
	this._current_path = cp;
};

Curve.prototype.currentPath = function(){
	return this._current_path;
};

Curve.prototype.append = function(point) {
	if (!(this._current_path in this._path)) {
		this._path[this._current_path] = new Array();
	}
	this._path[this._current_path].push(point);
};

Curve.prototype.path = function() {
	return this._path[0];
};

Curve.prototype.setCanvas = function(canvas) {
	this._canvas = canvas;
};

Curve.prototype.getCanvas = function(){
	return this._canvas;
};

Curve.prototype.setFollower = function(flwr){
	this._follower = flwr;
};

Curve.prototype.follower = function(){
	return this._follower;
};




// var Singleton = (function(){
// 	var _canvas = null;

// 	return{
// 		getInsance: function(canvas = null){
// 			if(!_canvas){
// 				_canvas = canvas;
// 			}
// 			return _canvas;
// 		}
// 	};
// })();
