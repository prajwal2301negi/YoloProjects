 # def display_fps(self, im0):
    #     """Displays the FPS on an image `im0` by calculating and overlaying as white text on a black rectangle."""
    #     self.end_time = time()
    #     fps = 1 / round(self.end_time - self.start_time, 2)
    #     text = f"FPS: {int(fps)}"
    #     text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)[0]
    #     gap = 10
    #     cv2.rectangle(
    #         im0,
    #         (20 - gap, 70 - text_size[1] - gap),
    #         (20 + text_size[0] + gap, 70 + gap),
    #         (255, 255, 255),
    #         -1,
    #     )
    #     cv2.putText(im0, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)