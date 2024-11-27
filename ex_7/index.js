document.getElementById('registerForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form submission
  
    // Get form fields
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');
  
    // Clear all error messages
    const errorMessages = document.querySelectorAll('.error-message');
    errorMessages.forEach((message) => (message.innerText = ''));
  
    // Validation flags
    let isValid = true;
  
    // Username Validation
    if (username.value.trim() === '') {
      setError(username, 'Username is required');
      isValid = false;
    } else if (username.value.length < 3) {
      setError(username, 'Username must be at least 3 characters long');
      isValid = false;
    } else {
      setSuccess(username);
    }
  
    // Email Validation
    if (email.value.trim() === '') {
      setError(email, 'Email is required');
      isValid = false;
    } else if (!isValidEmail(email.value)) {
      setError(email, 'Email is not valid');
      isValid = false;
    } else {
      setSuccess(email);
    }
  
    // Password Validation
    if (password.value.trim() === '') {
      setError(password, 'Password is required');
      isValid = false;
    } else if (password.value.length < 6) {
      setError(password, 'Password must be at least 6 characters long');
      isValid = false;
    } else {
      setSuccess(password);
    }
  
    // Confirm Password Validation
    if (confirmPassword.value.trim() === '') {
      setError(confirmPassword, 'Please confirm your password');
      isValid = false;
    } else if (confirmPassword.value !== password.value) {
      setError(confirmPassword, 'Passwords do not match');
      isValid = false;
    } else {
      setSuccess(confirmPassword);
    }
  
    // If all validations pass
    if (isValid) {
      alert('Registration Successful');
      // Optionally, submit the form here using AJAX or similar.
    }
  });
  
  // Helper Functions
  function setError(input, message) {
    const formGroup = input.parentElement;
    const errorMessage = formGroup.querySelector('.error-message');
    errorMessage.innerText = message;
    errorMessage.style.display = 'block';
  }
  
  function setSuccess(input) {
    const formGroup = input.parentElement;
    const errorMessage = formGroup.querySelector('.error-message');
    errorMessage.style.display = 'none';
  }
  
  function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }
  