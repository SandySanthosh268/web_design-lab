// Fetch posts data from JSONPlaceholder API
fetch('https://jsonplaceholder.typicode.com/posts')
  .then((response) => response.json())
  .then((data) => {
    const postsContainer = document.getElementById('posts-container');
    data.forEach((post) => {
      // Create a card for each post
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <h3>${post.title}</h3>
        <p>${post.body}</p>
      `;
      postsContainer.appendChild(card);
    });
  })
  .catch((error) => {
    console.error('Error fetching posts:', error);
    const postsContainer = document.getElementById('posts-container');
    postsContainer.innerHTML = '<p>Error loading posts. Please try again later.</p>';
  });
