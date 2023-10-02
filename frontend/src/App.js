import React, { useState, useEffect } from 'react';

function App() {
  const [bookData, setBookData] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [selectedBook, setSelectedBook] = useState(null); // شی کتاب انتخاب شده

  useEffect(() => {
    // تابع برای انجام درخواست GET برای دریافت اطلاعات کتاب
    const fetchBookData = () => {
      return fetch('/api/data/content/books/') // آدرس API GET برای اطلاعات کتاب را جایگزین کنید
        .then(response => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Failed to fetch book data');
          }
        });
    };

    // تابع برای انجام عملیات ورود (login)
    const performLogin = () => {
      // اطلاعات ورود کاربر را به صورت یک شی JSON تعریف کنید
      const userData = {
        username: 'ali',
        password: 'ali0013khani',
        // دیگر اطلاعات ورود
      };
    
      // تنظیمات درخواست POST
      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData), // تبدیل اطلاعات به رشته JSON و ارسال آن به عنوان بدن درخواست
      };
    
      // انجام درخواست POST به آدرس `/admin/` (آدرس واقعی API خود را جایگزین کنید)
      return fetch('/admin/', requestOptions)
        .then(response => {
          if (response.ok) {
            return true; // ورود موفقیت‌آمیز بوده است
          } else {
            throw new Error('Login failed');
          }
        });
    };
    

    // استفاده از Promise.all برای انجام همزمان دو درخواست GET و login
    Promise.all([fetchBookData(), performLogin()])
      .then(([bookData, loginResult]) => {
        setBookData(bookData);
        setIsLoggedIn(loginResult);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }, []);

  // تابع برای تنظیم کتاب انتخاب شده
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

export default App;
