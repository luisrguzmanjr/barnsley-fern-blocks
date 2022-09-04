controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    drawFern()
})
function drawFern () {
    x = [0]
    y = [0]
    for (let index = 0; index <= 99; index++) {
        z = randint(1, 100)
        if (z == 1) {
            x.push(0)
            y.push(0.16 * y[index])
        }
        if (z >= 2 && z <= 86) {
            x.push(0.85 * x[index] + 0.04 * y[index])
            y.push(-0.04 * x[index] + 0.85 * y[index] + 1.6)
        }
        if (z >= 87 && z <= 93) {
            x.push(0.2 * x[index] - 0.26 * y[index])
            y.push(0.23 * x[index] + 0.22 * y[index] + 1.6)
        }
        if (z >= 94 && z <= 100) {
            x.push(-0.15 * x[index] + 0.28 * y[index])
            y.push(0.26 * x[index] + 0.24 * y[index] + 0.44)
        }
        ix = width / 2 + x[index] * width / 10
        iy = y[index] * height / 12
        fern.setPixel(ix, iy, 7)
    }
}
let iy = 0
let ix = 0
let z = 0
let y: number[] = []
let x: number[] = []
let fern: Image = null
let height = 0
let width = 0
width = 100
height = 100
fern = image.create(width, height)
let showFern = sprites.create(fern, SpriteKind.Player)
