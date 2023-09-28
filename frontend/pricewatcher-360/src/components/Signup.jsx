import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";

const Signup = () => {
  // Validation schema using Yup
  const validationSchema = Yup.object({
    username: Yup.string().required("Username is required"),
    email: Yup.string()
      .email("Invalid email address")
      .required("Email is required"),
    password: Yup.string().required("Password is required"),
    confirmPassword: Yup.string()
      .oneOf([Yup.ref("password"), null], "Passwords must match")
      .required("Confirm Password is required"),
  });

  // Formik hook
  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    },
    validationSchema: validationSchema,
    onSubmit: async (values) => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/signup/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values),
        });

        if (!response.ok) {
          // Handle the case where the server returns an error
          const errorData = await response.json();
          console.error("Server error:", errorData);
          // You might want to update the state or display an error message to the user
        } else {
          // Handle the case where the server successfully processes the data
          const data = await response.json();
          console.log("Data sent to the backend:", data);
          // You might want to update the state or navigate to a new page
        }
      } catch (error) {
        console.error("Error sending data to the backend:", error);
        // You might want to update the state or display an error message to the user
      }
    },
  });

  return (
    <div className="flex items-center justify-center mt-8">
      <div className="w-full max-w-lg">
        <form
          onSubmit={formik.handleSubmit}
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
                formik.touched.username && formik.errors.username
                  ? "border-red-500"
                  : ""
              }`}
              name="username"
              value={formik.values.username}
              onChange={formik.handleChange}
              type="text"
              required
              placeholder="Username"
            />
            {formik.touched.username && formik.errors.username && (
              <p className="text-red-500 text-xs italic">
                {formik.errors.username}
              </p>
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
                formik.touched.email && formik.errors.email
                  ? "border-red-500"
                  : ""
              }`}
              name="email"
              value={formik.values.email}
              onChange={formik.handleChange}
              type="email"
              required
              placeholder="Email"
            />
            {formik.touched.email && formik.errors.email && (
              <p className="text-red-500 text-xs italic">
                {formik.errors.email}
              </p>
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
                formik.touched.password && formik.errors.password
                  ? "border-red-500"
                  : ""
              }`}
              type="password"
              placeholder="Password"
              name="password"
              value={formik.values.password}
              onChange={formik.handleChange}
              required
              autoComplete="new-password"
            />
            {formik.touched.password && formik.errors.password && (
              <p className="text-red-500 text-xs italic">
                {formik.errors.password}
              </p>
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
                formik.touched.confirmPassword && formik.errors.confirmPassword
                  ? "border-red-500"
                  : ""
              }`}
              type="password"
              placeholder="Confirm Password"
              name="confirmPassword"
              value={formik.values.confirmPassword}
              onChange={formik.handleChange}
              required
              autoComplete="new-password"
            />
            {formik.touched.confirmPassword &&
              formik.errors.confirmPassword && (
                <p className="text-red-500 text-xs italic">
                  {formik.errors.confirmPassword}
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
