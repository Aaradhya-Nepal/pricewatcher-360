import React, { useState } from "react";

const Signup = () => {
  // State for form data
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  // State for validation errors
  const [errors, setErrors] = useState({});

  // Function to handle input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setForm((prevForm) => ({
      ...prevForm,
      [name]: value,
    }));
  };

  // Function to validate form data
  const validateForm = () => {
    const newErrors = {};

    // Basic validation: Check if fields are not empty
    Object.entries(form).forEach(([key, value]) => {
      if (!value.trim()) {
        newErrors[key] = `${key} is required`;
      }
    });

    setErrors(newErrors);

    // Return true if there are no errors
    return Object.keys(newErrors).length === 0;
  };

  // Function to handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate the form
    if (validateForm()) {
      // Add logic to send data to the Django backend (e.g., using fetch or axios)
      try {
        const response = await fetch("your-backend-api-endpoint", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(form),
        });

        // Handle the response (e.g., show success message)
        const data = await response.json();
        console.log("Data sent to the backend:", data);
      } catch (error) {
        console.error("Error sending data to the backend:", error);
      }
    }
  };

  return (
    <div className="flex items-center justify-center mt-8">
      <div className="w-full max-w-lg">
        <form
          onSubmit={handleSubmit}
          className="bg-white rounded border-gray-300 border px-12 pt-6 pb-8 mb-4"
        >
          <div className="text-gray-800 text-2xl flex justify-center py-2 mb-4">
            Sign Up
          </div>
          <div className="mb-4">
            <label
              className="block text-gray-700 text-sm font-normal mb-2"
              htmlFor="username"
            >
              Username
            </label>
            <input
              className={`appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ${
                errors.username ? "border-red-500" : ""
              }`}
              name="username"
              value={form.username}
              onChange={handleInputChange}
              type="text"
              required
              placeholder="Username"
            />
            {errors.username && (
              <p className="text-red-500 text-xs italic">{errors.username}</p>
            )}
          </div>
          <div className="mb-4">
            <label
              className="block text-gray-700 text-sm font-normal mb-2"
              htmlFor="email"
            >
              Email
            </label>
            <input
              className={`appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ${
                errors.email ? "border-red-500" : ""
              }`}
              name="email"
              value={form.email}
              onChange={handleInputChange}
              type="email"
              required
              placeholder="Email"
            />
            {errors.email && (
              <p className="text-red-500 text-xs italic">{errors.email}</p>
            )}
          </div>
          <div className="mb-4">
            <label
              className="block text-gray-700 text-sm font-normal mb-2"
              htmlFor="password"
            >
              Password
            </label>
            <input
              className={`appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline ${
                errors.password ? "border-red-500" : ""
              }`}
              type="password"
              placeholder="Password"
              name="password"
              value={form.password}
              onChange={handleInputChange}
              required
              autoComplete="new-password"
            />
            {errors.password && (
              <p className="text-red-500 text-xs italic">{errors.password}</p>
            )}
          </div>
          <div className="mb-6">
            <label
              className="block text-gray-700 text-sm font-normal mb-2"
              htmlFor="confirmPassword"
            >
              Confirm Password
            </label>
            <input
              className={`appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline ${
                errors.confirmPassword ? "border-red-500" : ""
              }`}
              type="password"
              placeholder="Confirm Password"
              name="confirmPassword"
              value={form.confirmPassword}
              onChange={handleInputChange}
              required
              autoComplete="new-password"
            />
            {errors.confirmPassword && (
              <p className="text-red-500 text-xs italic">
                {errors.confirmPassword}
              </p>
            )}
          </div>
          <div className="flex items-center justify-between">
            <button
              className="px-4 py-2 rounded text-white inline-block bg-primary-color hover:bg-secondary-color focus:bg-secondary-color"
              type="submit"
            >
              Sign Up
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Signup;
