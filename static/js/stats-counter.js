// Stats Counter Animation
document.addEventListener('DOMContentLoaded', function() {
    const stats = document.querySelectorAll('.stats-opt-7 .num');
    let hasAnimated = false;

    function animateCount(element) {
        const target = parseFloat(element.getAttribute('data-target'));
        const suffix = element.getAttribute('data-suffix') || '';
        const duration = 2000; // 2 seconds
        const frameRate = 1000 / 60; // 60 FPS
        const totalFrames = Math.round(duration / frameRate);
        const increment = target / totalFrames;
        
        let currentCount = 0;
        let frame = 0;

        const counter = setInterval(() => {
            frame++;
            currentCount += increment;
            
            if (frame >= totalFrames) {
                currentCount = target;
                clearInterval(counter);
            }

            // Format the number
            let displayValue;
            if (target >= 1 && target < 100) {
                // Whole numbers (10, 26, 40)
                displayValue = Math.floor(currentCount);
            } else {
                // Decimal numbers (11.5)
                displayValue = currentCount.toFixed(1);
            }
            
            element.textContent = displayValue + suffix;
        }, frameRate);
    }

    // Intersection Observer to trigger animation when section is visible
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !hasAnimated) {
                hasAnimated = true;
                stats.forEach((stat, index) => {
                    setTimeout(() => {
                        animateCount(stat);
                    }, index * 100); // Stagger each stat by 100ms
                });
            }
        });
    }, {
        threshold: 0.5 // Trigger when 50% of the section is visible
    });

    // Observe the stats section
    const statsSection = document.querySelector('.stats-opt-7');
    if (statsSection) {
        observer.observe(statsSection);
    }
});
