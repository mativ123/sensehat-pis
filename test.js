var a = 1
var fuel = 20
var kml = 22
var v = 0
var d = 0
var t = 5

function main() {
    v += a;
    v_km_per_s = v / 1000;
    d += v_km_per_s;
    fuel_consumption = v_km_per_s / kml;
    t -= fuel_consumption;

    document.getElementById("hastighed").innerHTML = v;
    document.getElementById("distance").innerHTML = d;
    document.getElementById("tank").innerHTML = t;
    console.log(`fart[m/s]: ${v}, km kørt: ${d}, tanken[l]: ${t}`);
    if(t > 0) { 
        setTimeout(main, 1000);
    } else {
        console.log("Tanken er tom");
    }
    
}

main();