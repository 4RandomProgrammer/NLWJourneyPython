import { FormEvent, useState } from "react";
import { ConfirmGuestModal } from "./confirm-guest-modal";

export function GuestConfirmationPage() {
  const [guestName, setGuestName] = useState("");
  const [guestEmail, setGuestEmail] = useState("");
  const [isConfirmGuestModalOpen, setIsConfirmGuestModalOpen] = useState(true);

  function closeConfirmGuestModal() {
    setIsConfirmGuestModalOpen(false);
  }

  function createGuest(e: FormEvent<HTMLFormElement>) {
    return;
  }

  return (
    <ConfirmGuestModal
      setGuestName={setGuestEmail}
      setGuestEmail={setGuestEmail}
      closeConfirmParticipantModal={closeConfirmGuestModal}
      createParticipant={createGuest}
    />
  );
}
