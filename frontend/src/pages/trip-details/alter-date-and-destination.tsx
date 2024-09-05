import { Calendar, MapPin, X } from "lucide-react";
import { FormEvent, useEffect, useState } from "react";
import { api } from "../../lib/axios";
import { useNavigate, useParams } from "react-router-dom";
import { Button } from "../../components/button";
import { TripData } from "./destination-and-date-header";
import { DateRange, DayPicker } from "react-day-picker";
import { format } from "date-fns";

interface AlterDateAndDestinationModalProps {
  closeAlterDateAndDestinationModal: () => void;
}

export function AlterDateAndDestinationModal({
  closeAlterDateAndDestinationModal,
}: AlterDateAndDestinationModalProps) {
  const navigate = useNavigate();
  const { tripId } = useParams();
  const [isDatePickerOpen, setIsDatePickerOpen] = useState(false);
  const [destination, setDestination] = useState("");
  const [trip, setTrip] = useState<TripData | undefined>();
  const [eventStartAndEndDates, setEventStartAndEndDates] = useState<
    DateRange | undefined
  >();

  function openDatePicker(e: MouseEvent) {
    e.preventDefault();
    setIsDatePickerOpen(true);
  }

  function closeDatePicker() {
    setIsDatePickerOpen(false);
  }

  useEffect(() => {
    api.get(`/trips/${tripId}`).then((response) => {
      setTrip(response.data.trip);

      if (
        response.data.trip &&
        response.data.trip.starts_at &&
        response.data.trip.ends_at
      ) {
        const initialValue: DateRange = {
          from: new Date(response.data.trip.starts_at),
          to: new Date(response.data.trip.ends_at),
        };
        setDestination(response.data.trip.destination);
        setEventStartAndEndDates(initialValue);
      }
    });
  }, []);

  async function alterTrip(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();

    if (!eventStartAndEndDates) {
      return;
    }

    if (!destination) {
      return;
    }
    const response = await api.post(
      `/trips/${tripId}/update_date_and_destination`,
      {
        tripId: tripId,
        destination: destination,
        start_date: eventStartAndEndDates.from,
        end_date: eventStartAndEndDates.to,
      }
    );

    window.document.location.reload();
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
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
      <div className="w-[640px] rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
        <div className="space-y-2">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">Alterar local e/ou data</h2>
            <button type="button">
              <X
                onClick={closeAlterDateAndDestinationModal}
                className="size-5 text-zinc-400"
              />
            </button>
          </div>
          <p className="text-sm text-zinc-400">
            Inclua os dados que deseja alterar
          </p>
        </div>
        <div className="flex flex-wrap gap-2"></div>

        <form onSubmit={alterTrip} className="space-y-3">
          <div className="h-14 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2 items-center">
            <MapPin className="text-zinc-400 size-5" />
            <input
              name="place"
              placeholder="Qual o seu destino?"
              className="bg-transparent text-lg placeholder-zinc-400 outline-none flex-1"
              onChange={(event) => setDestination(event.target.value)}
              defaultValue={trip?.destination}
            />
          </div>

          <div className="h-14 p-4 bg-zinc-950 border border-zinc-800 rounded-lg flex gap-2">
            <button
              onClick={(event) => openDatePicker(event)}
              className="flex items-center gap-2 text-left w-[240px]"
            >
              <Calendar className="size-5s text-zinc-400" />
              <span className="text-lg text-zinc-400 w-40 flex-1">
                {displayedDate}
              </span>
            </button>
          </div>

          <Button type="submit" variant="primary" size="full">
            Confirmar alteração da viagem
          </Button>
        </form>
      </div>

      {isDatePickerOpen && (
        <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
          <div className="rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <h2 className="text-lg font-semibold">Selecione a data</h2>
                <button type="button">
                  <X
                    onClick={closeDatePicker}
                    className="size-5 text-zinc-400"
                  />
                </button>
              </div>
            </div>

            <DayPicker
              mode="range"
              selected={eventStartAndEndDates}
              onSelect={setEventStartAndEndDates}
            />
          </div>
        </div>
      )}
    </div>
  );
}
