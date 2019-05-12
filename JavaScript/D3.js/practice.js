// import "./D3Library/d3.js";

function SimpleWidget(spec) {
  let instance = {};
  let headline, description;
  instance.render = function() {
    let div = d3.select("body").append("div");
    div.append("h3").text(headline);
    div
      .attr("class", "box")
      .attr("style", "color:" + spec.color)
      .append("p")
      .text(description);
    return instance;
  };
  instance.headline = function(h) {
    if (!arguments.length) return headline;
    console.log(arguments)
    headline = h;
    return instance;
  };
  instance.description = function(d) {
    if (!arguments.length) return description;
    description = d;
    return instance;
  };

  return instance;
}

let widget = SimpleWidget({ color: "#6495ed" })
  .headline("Simple Widget")
  .description("This is a simple widget demonstrating functional javascript.");
widget.render();
