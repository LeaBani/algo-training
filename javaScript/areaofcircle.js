var circleArea = function(radius) {
    if (radius > 0) {
      const area = Math. PI * (radius * radius);
        return Number(area.toFixed(2));
    } else {
        return false;
    }
};



// area = π × R²

circleArea(-1485.86);    //returns false
circleArea(0);           //returns false
circleArea(43.2673);     //returns 5881.25
circleArea(68);          //returns 14526.72
circleArea("number");    //returns false