import React, { useState, useEffect } from 'react';

function App() {
  const [bookData, setBookData] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [selectedBook, setSelectedBook] = useState(null); 

  useEffect(() => {
    const fetchBookData = () => {
      return fetch('/api/data/content/books/') 
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Failed to fetch book data');
          }
        });
    };

    const performLogin = () => {
      const userData = {
        username: 'ali',
        password: 'ali0013khani',
      };
    
      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData), 
      };
    
      return fetch('/admin/', requestOptions)
        .then(response => {
          if (response.ok) {
            return true; 
          } else {
            throw new Error('Login failed');
          }
        });
    };
    

    Promise.all([fetchBookData(), performLogin()])
      .then(([bookData, loginResult]) => {
        setBookData(bookData);
        setIsLoggedIn(loginResult);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []);

  const handleBookSelect = (bookName) => {
    const selected = bookData.find(book => book.name === bookName);
    setSelectedBook(selected);
  };

  return (
    <div className="App">
      <header className="App-header">
        {isLoggedIn ? (
          <div>
            {selectedBook ? (
              <div>
                <h1>Selected Book Data</h1>
                <p>Title: {selectedBook.name}</p>
                <p>Author: {selectedBook.author}</p>
                {/* دیگر اطلاعات کتاب */}
              </div>
            ) : (
              <div>
                <h1>Book List</h1>
                <ul>
                  {bookData.map((book, index) => (
                    <li key={index} onClick={() => handleBookSelect(book.name)}>
                      {book.name}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ) : (
          <p>Login failed. Please try again.</p>
        )}
      </header>
    </div>
  );
}
function data_element() {
  let data = document.querySelector('#data');
  let data_content = data.innerHTML;
  data.remove();
}
document.addEventListener('DOMContentLoaded' , data_element());
export default App;
