$(function() {
    var x = document.getElementById("length").innerHTML; 
    var y = document.getElementById("height").innerHTML;
    var white_color = [];
    for (var i = 0; i <= 99; ++i) {
        if (i < 10) {
            var a = "0" + i.toString();
        } else {
            var a = i.toString();
        }
        white_color.push(a);
    }
    document.getElementById("previous").innerHTML = [];
    var check = 0;
    document.addEventListener("mousemove", function(e) {
        if (check == 1) {
            var number = e.target.id;
            var a = Math.floor(number / 10);
            var b = number - a * 10;
            for (var l = 0; l <= 99; ++l) {
                if (white_color[l] != "-1") {
                    document.getElementById(white_color[l]).style.backgroundColor = "white";
                }
            }
            if (document.getElementById("previous").innerHTML[0] > a) {
                if (document.getElementById("previous").innerHTML[2] < b) {
                    for (var i = 0; i <= document.getElementById("previous").innerHTML[0] - a; ++i) {
                        for (var j = 0; j <= b - document.getElementById("previous").innerHTML[2]; ++j) {
                            var t_id = (document.getElementById("previous").innerHTML[0] - i).toString() + (b - j).toString();
                            document.getElementById(t_id).style.backgroundColor = '#cbc3f7';
                        }
                    }
                } else {
                    for (var i = 0; i <= document.getElementById("previous").innerHTML[0] - a; ++i) {
                        for (var j = 0; j <= document.getElementById("previous").innerHTML[2] - b; ++j) {
                            var t_id = (document.getElementById("previous").innerHTML[0] - i).toString() + (document.getElementById("previous").innerHTML[2] - j).toString();
                            document.getElementById(t_id).style.backgroundColor = '#cbc3f7';
                        }
                    }
                }
            } else {
                if (document.getElementById("previous").innerHTML[2] < b) {
                    for (var i = 0; i <= a - document.getElementById("previous").innerHTML[0]; ++i) {
                        for (var j = 0; j <= b - document.getElementById("previous").innerHTML[2]; ++j) {
                            var t_id = (a - i).toString() + (b - j).toString();
                            document.getElementById(t_id).style.backgroundColor = '#cbc3f7';
                        }
                    }
                } else {
                    for (var i = 0; i <= a - document.getElementById("previous").innerHTML[0]; ++i) {
                        for (var j = 0; j <= document.getElementById("previous").innerHTML[2] - b; ++j) {
                            var t_id = (a - i).toString() + (document.getElementById("previous").innerHTML[2] - j).toString();
                            document.getElementById(t_id).style.backgroundColor = '#cbc3f7';
                        }
                    }
                }
            };
        };
    });
    document.addEventListener("click", function (e) {
        var number = e.target.id;
        var a = Math.floor(number / 10);
        var b = number - a * 10;
        if (document.getElementById("previous").innerHTML == []) {
            document.getElementById("previous").innerHTML = [a, b];
            check = 1;
        } else {
            if (document.getElementById("previous").innerHTML[0] > a) {
                if (document.getElementById("previous").innerHTML[2] < b) {
                    for (var i = 0; i <= document.getElementById("previous").innerHTML[0] - a; ++i) {
                        for (var j = 0; j <= b - document.getElementById("previous").innerHTML[2]; ++j) {
                            var t_id = (document.getElementById("previous").innerHTML[0] - i).toString() + (b - j).toString();
                            document.getElementById(t_id).style.backgroundColor = '#cbc3f7';
                            for (var l = 0; l <= 99; ++l) {
                                if (white_color[l] === t_id) {
                                    white_color[l] = "-1";
                                }
                            }
                        }
                    }
                } else {
                    for (var i = 0; i <= document.getElementById("previous").innerHTML[0] - a; ++i) {
                        for (var j = 0; j <= document.getElementById("previous").innerHTML[2] - b; ++j) {
                            var t_id = (document.getElementById("previous").innerHTML[0] - i).toString() + (document.getElementById("previous").innerHTML[2] - j).toString();
                            document.getElementById(t_id).style.backgroundColor = '#cbc3f7';
                            for (var l = 0; l <= 99; ++l) {
                                if (white_color[l] === t_id) {
                                    white_color[l] = "-1";
                                }
                            }
                        }
                    }
                }
            } else {
                if (document.getElementById("previous").innerHTML[2] < b) {
                    for (var i = 0; i <= a - document.getElementById("previous").innerHTML[0]; ++i) {
                        for (var j = 0; j <= b - document.getElementById("previous").innerHTML[2]; ++j) {
                            var t_id = (a - i).toString() + (b - j).toString();
                            document.getElementById(t_id).style.backgroundColor = '#cbc3f7';
                            for (var l = 0; l <= 99; ++l) {
                                if (white_color[l] === t_id) {
                                    white_color[l] = "-1";
                                }
                            }
                        }
                    }
                } else {
                    for (var i = 0; i <= a - document.getElementById("previous").innerHTML[0]; ++i) {
                        for (var j = 0; j <= document.getElementById("previous").innerHTML[2] - b; ++j) {
                            var t_id = (a - i).toString() + (document.getElementById("previous").innerHTML[2] - j).toString();
                            document.getElementById(t_id).style.backgroundColor = '#cbc3f7';
                            for (var l = 0; l <= 99; ++l) {
                                if (white_color[l] === t_id) {
                                    white_color[l] = "-1";
                                }
                            }
                        }
                    }
                }
            };
            document.getElementById("previous").innerHTML = [];
            check = 0;
        };
    });
    $("#spinButton").click(function() {
		$.ajax({
		    url: "/take_numbers",
            data: {
                result: document.innerHTML
            },
		    dataType: "json",
			timeout: 1e4,
			success: function(result) {
                document.getElementById("length").innerHTML = "Доступно по вертикали - " + result.length;
                document.getElementById("height").innerHTML  = "Доступно по горизонтали - " + result.height;
			},
			error: function() {
				console.log("NET");
            }
        })
    });
});
