import { FormEvent, useState } from "react";
import { ConfirmGuestModal } from "./confirm-guest-modal";
import { redirect, useParams } from "react-router-dom";
import { api } from "../../lib/axios";

export function GuestConfirmationPage() {
  const { participantId } = useParams();
  const [guestName, setGuestName] = useState("");
  const [guestEmail, setGuestEmail] = useState("");
  const [isConfirmGuestModalOpen, setIsConfirmGuestModalOpen] = useState(true);

  function closeConfirmGuestModal() {
    setIsConfirmGuestModalOpen(false);
  }

  async function createGuest(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    const response_confirm = api.get(`/participants/${participantId}/confirm`);
  }

  return (
    <>
      {isConfirmGuestModalOpen && (
        <ConfirmGuestModal
          setGuestName={setGuestEmail}
          setGuestEmail={setGuestEmail}
          closeConfirmParticipantModal={closeConfirmGuestModal}
          createParticipant={createGuest}
        />
      )}
    </>
  );
}
