const canvas = document.getElementById("stars");

if (canvas) {
  const ctx = canvas.getContext("2d");
  let stars = [];
  let width = 0;
  let height = 0;
  const STAR_COUNT = 140;

  function resizeCanvas() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }

  class Star {
    constructor() {
      this.reset();
      this.y = Math.random() * height;
    }

    reset() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.radius = Math.random() * 1.4 + 0.2;
      this.alpha = Math.random() * 0.8 + 0.1;
      this.speed = Math.random() * 0.08 + 0.01;
      this.twinkle = Math.random() * 0.02 + 0.003;
      this.direction = Math.random() > 0.5 ? 1 : -1;
    }

    update() {
      this.alpha += this.twinkle * this.direction;

      if (this.alpha >= 1) this.direction = -1;
      if (this.alpha <= 0.15) this.direction = 1;

      this.y += this.speed;

      if (this.y > height + 2) {
        this.y = -2;
        this.x = Math.random() * width;
      }
    }

    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,255,255,${this.alpha})`;
      ctx.fill();
    }
  }

  function initStars() {
    stars = [];
    for (let i = 0; i < STAR_COUNT; i++) {
      stars.push(new Star());
    }
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);

    for (const star of stars) {
      star.update();
      star.draw();
    }

    requestAnimationFrame(animate);
  }

  resizeCanvas();
  initStars();
  animate();

  window.addEventListener("resize", () => {
    resizeCanvas();
    initStars();
  });
}