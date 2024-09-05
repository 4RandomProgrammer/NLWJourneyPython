import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";
import { InviteGuestsModal } from "../../components/invite-guests-modal";
import { ConfirmTripModal } from "./confirm-trip-modal";
import { DestinationAndDateStep } from "./steps/destination-and-date-step";
import { InviteGuestsStep } from "./steps/invite-guests-step";
import { DateRange } from "react-day-picker";
import { api } from "../../lib/axios";
import { format } from "date-fns";

export function CreateTripPage() {
  const navigate = useNavigate();
  const [isGuestsInputOpen, setIsGuestsInputOpen] = useState(false);
  const [isGuestsModalOpen, setIsGuestsModalOpen] = useState(false);
  const [isConfirmTripModalOpen, setisConfirmTripModalOpen] = useState(false);
  const [emailsToInvite, setEmailsToInvite] = useState([]);
  const [destination, setDestination] = useState("");
  const [ownerName, setOwnerName] = useState("");
  const [ownerEmail, setOwnerEmail] = useState("");
  const [eventStartAndEndDates, setEventStartAndEndDates] = useState<
    DateRange | undefined
  >();

  function openGuestsInput() {
    setIsGuestsInputOpen(true);
  }

  function closeGuestsInput() {
    setIsGuestsInputOpen(false);
  }

  function openGuestsModal() {
    setIsGuestsModalOpen(true);
  }

  function closeGuestsModalt() {
    setIsGuestsModalOpen(false);
  }

  function openConfirmTripModal() {
    setisConfirmTripModalOpen(true);
  }

  function closeConfirmTripModal() {
    setisConfirmTripModalOpen(false);
  }

  function addNewEmailToInvite(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    const data = new FormData(e.currentTarget);
    const email = data.get("email");

    if (!email) {
      return;
    }

    if (emailsToInvite.includes(email)) {
      return;
    }

    setEmailsToInvite([...emailsToInvite, email]);

    e.currentTarget.reset();
  }

  function removeEmailtoInvite(emailToRemove: string) {
    const newEmailList = emailsToInvite.filter(
      (invited) => invited != emailToRemove
    );

    setEmailsToInvite(newEmailList);
  }

  async function createTrip(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    if (!destination) {
      return;
    }

    if (!eventStartAndEndDates?.from || !eventStartAndEndDates.to) {
      return;
    }

    if (emailsToInvite.length === 0) {
      return;
    }

    if (!ownerName || !ownerName) {
      return;
    }

    const response = await api.post("/trips", {
      destination: destination,
      start_date: eventStartAndEndDates.from,
      end_date: eventStartAndEndDates.to,
      owner_name: ownerName,
      owner_email: ownerEmail,
      emails_to_invite: emailsToInvite,
    });

    const { id } = response.data;
    navigate(`/trips/${id}`);
  }

  const displayedDate =
    eventStartAndEndDates &&
    eventStartAndEndDates.from &&
    eventStartAndEndDates.to
      ? format(eventStartAndEndDates.from, "d 'de' MMM")
          .concat(" até ")
          .concat(format(eventStartAndEndDates.to, "d 'de' MMM"))
      : "Quando?";

  return (
    <div className="h-screen flex items-center justify-center bg-pattern bg-no-repeat bg-center">
      <div className="max-w-3xl w-full px-6 text-center space-y-10">
        <div className="flex flex-col items-center gap-3">
          <img src="./public/logo.svg" alt="plann.er" />
          <p className="text-zinc-300 text-lg">
            Convide seus amigos e planeje sua próxima viagem!
          </p>
        </div>
        <div className="space-y-4">
          <DestinationAndDateStep
            isGuestsInputOpen={isGuestsInputOpen}
            closeGuestsInput={closeGuestsInput}
            openGuestsInput={openGuestsInput}
            setDestination={setDestination}
            eventStartAndEndDates={eventStartAndEndDates}
            setEventStartAndEndDates={setEventStartAndEndDates}
          />
          {isGuestsInputOpen ? (
            <InviteGuestsStep
              emailsToInvite={emailsToInvite}
              openConfirmTripModal={openConfirmTripModal}
              openGuestsModal={openGuestsModal}
            />
          ) : null}
        </div>
        <p className="text-sm text-zinc-500">
          Ao planejar sua viagem pela plann.er você automaticamente concorda{" "}
          <br /> com nossos{" "}
          <a
            href="#"
            className="text-zinc-300 underline"
            target="_blank"
            rel="noopener noreferrer"
          >
            termos de uso
          </a>{" "}
          e{" "}
          <a
            href="#"
            className="text-zinc-300 underline"
            target="_blank"
            rel="noopener noreferrer"
          >
            políticas de privacidade
          </a>
          .
        </p>
      </div>
      {isGuestsModalOpen && (
        <InviteGuestsModal
          addNewEmailToInvite={addNewEmailToInvite}
          emailsToInvite={emailsToInvite}
          closeGuestsModalt={closeGuestsModalt}
          removeEmailtoInvite={removeEmailtoInvite}
        />
      )}

      {isConfirmTripModalOpen && (
        <ConfirmTripModal
          createTrip={createTrip}
          closeConfirmTripModal={closeConfirmTripModal}
          setOwnerName={setOwnerName}
          setOwnerEmail={setOwnerEmail}
          destination={destination}
          tripDate={displayedDate}
        />
      )}
    </div>
  );
}
