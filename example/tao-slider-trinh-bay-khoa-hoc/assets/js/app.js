function init() {
  const slider = document.querySelector(".slider");
  const nextBtn = slider.querySelector(".slider .nav .next");
  const prevBtn = slider.querySelector(".slider .nav .prev");
  const items = slider.querySelectorAll(".slider .item");

  let current = 0;

  items.forEach((item) => {
    const textWrapper = item.querySelector(".wrap");
    textWrapper.innerHTML = textWrapper.textContent.replace(
      /\S/g,
      "<span class='letter'>$&</span>"
    );
  });

  function anim(current, next, callback) {
    const currentImgs = current.querySelectorAll(".img");
    const currentText = current.querySelectorAll(".content .letter");
    const nextImgs = next.querySelectorAll(".img");
    const nextText = next.querySelectorAll(".content .letter");

    const t = 400;
    const offset = "-=" + t * 0.4;
    const imgOffset = t * 0.8;

    const tl = anime.timeline({
      easing: "easeInOutQuint",
      duration: t,
      complete: callback,
    });

    // Add children
    tl.add({
      targets: currentText,
      translateY: [0, "-.75em"],
      /*clipPath: ['polygon(0 0, 100% 0, 100% 100%, 0% 100%)', 'polygon(0 100%, 100% 100%, 100% 100%, 0% 100%)'],*/
      opacity: [1, 0],
      easing: "easeInQuint",
      duration: t,
      delay: (el, i) => 10 * (i + 1),
    })
      .add(
        {
          targets: currentImgs[0],
          translateY: -600,
          translateZ: 0,
          rotate: [0, "-15deg"],
          opacity: [1, 0],
          easing: "easeInCubic",
        },
        offset
      )
      .add(
        {
          targets: currentImgs[1],
          translateY: -600,
          translateZ: 0,
          rotate: [0, "15deg"],
          opacity: [1, 0],
          easing: "easeInCubic",
        },
        "-=" + imgOffset
      )
      .add(
        {
          targets: currentImgs[2],
          translateY: -600,
          translateZ: 0,
          rotate: [0, "-15deg"],
          opacity: [1, 0],
          easing: "easeInCubic",
        },
        "-=" + imgOffset
      )
      .add(
        {
          targets: currentImgs[3],
          translateY: -600,
          translateZ: 0,
          rotate: [0, "15deg"],
          opacity: [1, 0],
          easing: "easeInCubic",
        },
        "-=" + imgOffset
      )
      .add({
        targets: current,
        opacity: 0,
        visibility: "hidden",
        duration: 10,
        easing: "easeInCubic",
      })
      .add(
        {
          targets: next,
          opacity: 1,
          visibility: "visible",
          duration: 10,
        },
        offset
      )
      .add(
        {
          targets: nextImgs[0],
          translateY: [600, 0],
          translateZ: 0,
          rotate: ["15deg", 0],
          opacity: [0, 1],
          easing: "easeOutCubic",
        },
        offset
      )
      .add(
        {
          targets: nextImgs[1],
          translateY: [600, 0],
          translateZ: 0,
          rotate: ["-15deg", 0],
          opacity: [0, 1],
          easing: "easeOutCubic",
        },
        "-=" + imgOffset
      )
      .add(
        {
          targets: nextImgs[2],
          translateY: [600, 0],
          translateZ: 0,
          rotate: ["15deg", 0],
          opacity: [0, 1],
          easing: "easeOutCubic",
        },
        "-=" + imgOffset
      )
      .add(
        {
          targets: nextImgs[3],
          translateY: [600, 0],
          translateZ: 0,
          rotate: ["-15deg", 0],
          opacity: [0, 1],
          easing: "easeOutCubic",
        },
        "-=" + imgOffset
      )
      .add(
        {
          targets: nextText,
          translateY: [".75em", 0],
          translateZ: 0,
          /*clipPath: ['polygon(0 0, 100% 0, 100% 0, 0 0)','polygon(0 0, 100% 0, 100% 100%, 0% 100%)'],*/
          opacity: [0, 1],
          easing: "easeOutQuint",
          duration: t * 1.5,
          delay: (el, i) => 10 * (i + 1),
        },
        offset
      );
  }

  let isPlaying = false;

  function updateSlider(newIndex) {
    const currentItem = items[current];
    const newItem = items[newIndex];

    function callback() {
      currentItem.classList.remove("is-active");
      newItem.classList.add("is-active");
      current = newIndex;
      isPlaying = false;
    }

    anim(currentItem, newItem, callback);
  }

  function next() {
    if (isPlaying) return;
    isPlaying = true;
    const newIndex = current === items.length - 1 ? 0 : current + 1;
    updateSlider(newIndex);
  }

  function prev() {
    if (isPlaying) return;
    isPlaying = true;
    const newIndex = current === 0 ? items.length - 1 : current - 1;
    updateSlider(newIndex);
  }

  nextBtn.onclick = next;
  prevBtn.onclick = prev;
}

document.addEventListener("DOMContentLoaded", init);
