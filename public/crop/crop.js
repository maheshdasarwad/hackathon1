document.addEventListener('DOMContentLoaded', function() {
    const loadMoreButton = document.getElementById('loadMore');
    const hiddenCards = document.querySelectorAll('.card.hidden');
  
    loadMoreButton.addEventListener('click', function() {
      hiddenCards.forEach(card => {
        card.classList.remove('hidden');
      });
      loadMoreButton.style.display = 'none';
    });
  });

document.getElementsByClassName('home')[0].addEventListener('click', function() {
    window.location.href = '/index/index.html';
});

document.getElementById("soyabean").addEventListener("click", () => {
  window.location.href = '/showTask.html';
})

document.getElementById("cotton").addEventListener("click", () => {
  window.location.href = '/cotton.html';
})

document.getElementById("jowar").addEventListener("click", () => {
  window.location.href = '/jowar.html';
})

document.addEventListener('DOMContentLoaded', function() {
  const loadMoreButton = document.getElementById('loadMore');
  const hiddenCards = document.querySelectorAll('.card.hidden');
  const addCropButton = document.querySelector('.card button'); // First button (Add Crop)
  const cardsContainer = document.querySelector('.cards-container');

  // Show hidden crop cards on clicking "Load More"
  loadMoreButton.addEventListener('click', function() {
      hiddenCards.forEach(card => {
          card.classList.remove('hidden');
      });
      loadMoreButton.style.display = 'none';
  });

  // Add new crop dynamically
  addCropButton.addEventListener('click', function() {
      const cropName = prompt("Enter crop name:");
      const cropDescription = prompt("Enter crop description:");

      if (cropName && cropDescription) {
          // Create new crop card
          const newCard = document.createElement('div');
          newCard.classList.add('card');

          newCard.innerHTML = `
              <h2>🌱 ${cropName}</h2>
              <p>${cropDescription}</p>
              <button>View Details</button>
          `;

          // Add new crop card to the container
          cardsContainer.appendChild(newCard);
      } else {
          alert("Crop name and description cannot be empty.");
      }
  });
});