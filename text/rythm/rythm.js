AFRAME.registerComponent("rythm", {
    schema: {
        bpm: { type: "number", default: 60 },
        beat: { type: "number", default: 4 },
    },
    init: function () {
        this.beat = 0;
        this.beatTime = 0;
        this.beatDuration = 60 / this.data.bpm;
        this.el.addEventListener("tick", this.tick.bind(this));

        // listen to the beat event
        this.el.addEventListener("beat", (event) => {
            console.log("beat", event.detail.beat);

            const random = Math.random() / 10;

            anime({
                targets: this.el.object3D.scale,
                x: [1, 1 + random, 1],
                y: [1, 1 + random, 1],
                z: [1, 1 + random, 1],
                easing: "easeInOutExpo",
                duration: (60 / this.data.bpm) * 1000 * 0.5,
            });
        });
    },
    tick: function (time, timeDelta) {
        this.beatTime += timeDelta / 1000;
        if (this.beatTime >= this.beatDuration) {
            this.beatTime -= this.beatDuration;
            this.beat = (this.beat + 1) % this.data.beat;
            this.el.emit("beat", { beat: this.beat });
        }
    },
});
