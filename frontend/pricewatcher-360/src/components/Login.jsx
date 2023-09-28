import React, { useState } from "react";

const Login = () => {
  // State for form data
  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  // Function to handle input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setForm((prevForm) => ({
      ...prevForm,
      [name]: value,
    }));
  };

  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // Add logic for form submission (e.g., API call or other actions)
  };

  return (
    <div className="flex items-center justify-center mt-8">
      <div className="w-full max-w-lg">
        <form
          onSubmit={handleSubmit}
          className="bg-white rounded border-gray-300 border px-12 pt-6 pb-8 mb-4"
        >
          <div className="text-gray-800 text-2xl flex justify-center py-2 mb-4">
            Login
          </div>
          <div className="mb-4">
            <label
              className="block text-gray-700 text-sm font-normal mb-2"
              htmlFor="email"
            >
              Email
            </label>
            <input
              className="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              name="email"
              value={form.email}
              onChange={handleInputChange}
              type="email"
              required
              autoFocus
              placeholder="Email"
            />
          </div>
          <div className="mb-6">
            <label
              className="block text-gray-700 text-sm font-normal mb-2"
              htmlFor="password"
            >
              Password
            </label>
            <input
              className="appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
              type="password"
              placeholder="Password"
              name="password"
              value={form.password}
              onChange={handleInputChange}
              required
              autoComplete="current-password"
            />
          </div>
          <div className="flex items-center justify-between">
            <button
              className="px-4 py-2 rounded text-white inline-block bg-primary-color hover:bg-secondary-color focus:bg-secondary-color"
              type="submit"
            >
              Sign In
            </button>
            <a
              className="inline-block align-baseline font-normal text-sm text-primary-color hover:text-secondary-color"
              href="#"
            >
              Forgot Password?
            </a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
