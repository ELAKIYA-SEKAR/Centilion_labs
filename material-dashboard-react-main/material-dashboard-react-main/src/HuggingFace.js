import React from "react";
import MDBox from "components/MDBox";

function huggingface() {
  return (
    <MDBox
      display="flex"
      justifyContent="center"
      alignItems="center"
      width="100%"
      height="3.25rem" // Adjust the height as needed for an oval shape
      bgColor="white"
      shadow="sm"
      borderRadius="50%" // Use border-radius to create an oval shape
    >
      <img
        src="hugging_face_image.jpg" // Replace with the image source
        alt="Hugging Face"
        width="50%" // Adjust the image size as needed
        height="auto" // Maintain the aspect ratio
      />
    </MDBox>
  );
}

export default huggingface;
