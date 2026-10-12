// Interactive behaviors for Evelin Lins Portfolio

document.addEventListener('DOMContentLoaded', () => {
  // 1. FAQ Accordion toggle
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      
      // Close other accordion items
      faqItems.forEach(otherItem => {
        if (otherItem !== item) {
          otherItem.classList.remove('active');
        }
      });
      
      // Toggle current item
      if (!isActive) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  });

  // 2. Smooth scrolling for internal anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // 3. Navbar scroll effect
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.style.boxShadow = '0 8px 24px rgba(32, 13, 35, 0.08)';
    } else {
      navbar.style.boxShadow = 'none';
    }
  });

  // 4. Subtle number counter animation on stats
  const statNumbers = document.querySelectorAll('.stat-number');
  let animated = false;

  const triggerAnimation = () => {
    if (animated) return;
    const statsSection = document.querySelector('.stats-strip');
    if (!statsSection) return;

    const rect = statsSection.getBoundingClientRect();
    if (rect.top <= window.innerHeight * 0.85) {
      animated = true;
      statNumbers.forEach(stat => {
        stat.style.opacity = '0';
        stat.style.transform = 'translateY(10px)';
        setTimeout(() => {
          stat.style.transition = 'all 0.6s ease';
          stat.style.opacity = '1';
          stat.style.transform = 'translateY(0)';
        }, 100);
      });
    }
  };

  window.addEventListener('scroll', triggerAnimation);
  triggerAnimation();
});
