import { useState } from "react";
import axios from "axios";
import React from "react";

function App() {
    const [file, setFile] = useState<File | null>(null);
    const [message, setMessage] = useState("");
    const [streak, setStreak] = useState<number | null>(null);
    const [loading, setLoading] = useState(false);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setFile(event.target.files[0]);
        }
    };

    const handleUpload = async () => {
        if (!file) {
            setMessage("⚠️ Please select a file first!");
            return;
        }

        const formData = new FormData();
        formData.append("image", file);

        setLoading(true); // Start loading

        try {
            const response = await axios.post("http://localhost:5000/upload", formData);
            setMessage(response.data.message);
            setStreak(response.data.streak);
        } catch (error) {
            setMessage("❌ Upload failed!");
        } finally {
            setLoading(false); // Stop loading
        }
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-6">
            <div className="bg-white shadow-lg rounded-lg p-6 w-full max-w-md text-center">
                <h2 className="text-2xl font-semibold text-gray-800 mb-4">
                    📸 Upload DSA Submission Screenshot
                </h2>

                <input
                    type="file"
                    accept="image/*"
                    onChange={handleFileChange}
                    className="mb-4 w-full border border-gray-300 p-2 rounded-lg"
                />

                <button
                    onClick={handleUpload}
                    disabled={loading}
                    className={`w-full py-2 rounded-lg font-semibold transition duration-300 ${
                        loading
                            ? "bg-gray-400 cursor-not-allowed"
                            : "bg-blue-500 text-white hover:bg-blue-600"
                    }`}
                >
                    {loading ? "⏳ Uploading..." : "🚀 Upload"}
                </button>

                {loading && <p className="mt-4 text-gray-700">⏳ Processing... Please wait.</p>}
                {!loading && message && <p className="mt-4 text-gray-700">{message}</p>}
                {!loading && streak !== null && (
                    <p className="mt-2 text-xl font-semibold text-orange-500">
                        🔥 Current Streak: {streak} Days
                    </p>
                )}
            </div>
        </div>
    );
}

export default App;
