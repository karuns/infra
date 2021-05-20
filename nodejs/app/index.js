const app = require("express")();


app.get("/",
    (req, res) => res.send("Hello from a lightweight node js container with app-" + between(1,100))
)

app.listen(9999, ()=> console.log("Listening on 9999"))


function between(min, max) {
  return Math.floor(
    Math.random() * (max - min + 1) + min
  )
}
