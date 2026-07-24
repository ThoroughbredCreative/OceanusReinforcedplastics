// Oceanus Reinforced Plastics — shared site behaviour
(function () {
  "use strict";

  /* Mobile nav toggle ----------------------------------------------------*/
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var isOpen = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      document.body.style.overflow = isOpen ? "hidden" : "";
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      });
    });
  }

  /* Scroll-spy nav highlighting ---------------------------------------------*/
  var navLinks = document.querySelectorAll("[data-nav-link]");
  var spySections = Array.prototype.slice
    .call(navLinks)
    .map(function (link) {
      var id = link.getAttribute("href").slice(1);
      return { link: link, section: document.getElementById(id) };
    })
    .filter(function (entry) { return entry.section; });

  if ("IntersectionObserver" in window && spySections.length) {
    var spyObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var match = spySections.find(function (s) { return s.section === entry.target; });
          if (!match) return;
          if (entry.isIntersecting) {
            navLinks.forEach(function (l) { l.classList.remove("active"); });
            match.link.classList.add("active");
          }
        });
      },
      { rootMargin: "-40% 0px -55% 0px" }
    );
    spySections.forEach(function (entry) { spyObserver.observe(entry.section); });
  }

  /* Scroll reveal ----------------------------------------------------------*/
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* FAQ accordion ----------------------------------------------------------*/
  document.querySelectorAll(".faq-question").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var expanded = btn.getAttribute("aria-expanded") === "true";
      var answer = document.getElementById(btn.getAttribute("aria-controls"));

      document.querySelectorAll(".faq-question").forEach(function (other) {
        if (other !== btn) {
          other.setAttribute("aria-expanded", "false");
          var otherAnswer = document.getElementById(other.getAttribute("aria-controls"));
          if (otherAnswer) otherAnswer.style.maxHeight = null;
        }
      });

      btn.setAttribute("aria-expanded", expanded ? "false" : "true");
      if (answer) answer.style.maxHeight = expanded ? null : answer.scrollHeight + "px";
    });
  });

  /* Gallery filter ----------------------------------------------------------*/
  var filterBar = document.querySelector(".filter-bar");
  if (filterBar) {
    var items = document.querySelectorAll(".gallery-item");
    filterBar.addEventListener("click", function (e) {
      var btn = e.target.closest(".filter-btn");
      if (!btn) return;
      filterBar.querySelectorAll(".filter-btn").forEach(function (b) {
        b.classList.remove("active");
        b.setAttribute("aria-pressed", "false");
      });
      btn.classList.add("active");
      btn.setAttribute("aria-pressed", "true");
      var category = btn.getAttribute("data-filter");
      items.forEach(function (item) {
        var show = category === "all" || item.getAttribute("data-category") === category;
        item.hidden = !show;
      });
    });
  }

  /* Contact form ----------------------------------------------------------*/
  var form = document.getElementById("contact-form");
  if (form) {
    var successBox = document.getElementById("form-success");

    function showError(field, message) {
      var wrap = field.closest(".field");
      wrap.classList.add("invalid");
      var errorEl = wrap.querySelector(".field-error");
      if (errorEl) errorEl.textContent = message;
    }
    function clearError(field) {
      var wrap = field.closest(".field");
      wrap.classList.remove("invalid");
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var valid = true;
      var requiredFields = form.querySelectorAll("[required]");

      requiredFields.forEach(function (field) {
        clearError(field);
        if (!field.value.trim()) {
          showError(field, "This field is required.");
          valid = false;
          return;
        }
        if (field.type === "email") {
          var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailPattern.test(field.value.trim())) {
            showError(field, "Enter a valid email address.");
            valid = false;
          }
        }
      });

      if (!valid) {
        var firstInvalid = form.querySelector(".invalid input, .invalid select, .invalid textarea");
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      form.reset();
      form.hidden = true;
      if (successBox) {
        successBox.classList.add("visible");
        successBox.focus();
      }
    });

    form.querySelectorAll("input, select, textarea").forEach(function (field) {
      field.addEventListener("input", function () { clearError(field); });
    });
  }
})();
