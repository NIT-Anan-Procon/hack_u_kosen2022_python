const canvas = document.getElementById("canvas");

function Test() {
  setInterval(() => {
    canvas
      .getContext("2d")
      .drawImage(
        video,
        0,
        0,
        canvas.width,
        canvas.height,
        0,
        0,
        canvas.width,
        canvas.height
      );
    fetch("http://202.231.44.30/measure-variable", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        image: canvas.toDataURL().replace(/^data:\w+\/\w+;base64,/, ""),
      }),
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        console.log(data["variable"]);
      });
  }, 2000);
}
