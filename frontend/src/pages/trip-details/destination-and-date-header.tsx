import { MapPin, Calendar, Settings2 } from "lucide-react";
import { Button } from "../../components/button";
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { api } from "../../lib/axios";
import { format } from "date-fns";
import { AlterDateAndDestinationModal } from "./alter-date-and-destination";

export interface TripData {
  destination: string;
  ends_at: string;
  id: string;
  starts_at: string;
  status: null | boolean;
}

export function DestinationAndDateHeader() {
  const { tripId } = useParams();
  const [trip, setTrip] = useState<TripData | undefined>();
  const [
    isAlterDateAndDestinationModalOpen,
    setIsAlterDateAndDestinationModalOpen,
  ] = useState(false);

  function openAlterDateAndDestionationModal() {
    setIsAlterDateAndDestinationModalOpen(true);
  }

  function closeAlterDateAndDestionationModal() {
    setIsAlterDateAndDestinationModalOpen(false);
  }

  useEffect(() => {
    api.get(`/trips/${tripId}`).then((response) => setTrip(response.data.trip));
  }, [tripId]);

  const displayedDate =
    trip && trip.starts_at && trip.ends_at
      ? format(trip.starts_at, "d 'de' MMM")
          .concat(" até ")
          .concat(format(trip.ends_at, "d 'de' MMM"))
      : null;

  return (
    <div className="px-4 h-16 rounded-xl bg-zinc-900 shadow-shape flex items-center justify-between">
      <div className="flex items-center gap-2">
        <MapPin className="size-5 text-zinc-400" />
        <span className="text-zinc-100">{trip?.destination}</span>
      </div>

      <div className="flex items-center gap-5">
        <div className="flex items-center gap-2">
          <Calendar className="size-5 text-zinc-400" />
          <span className="text-zinc-100">{displayedDate}</span>
        </div>

        <div className="w-px h-6 bg-zinc-800"></div>

        <Button onClick={openAlterDateAndDestionationModal} variant="secondary">
          Alterar local/data
          <Settings2 className="size-5" />
        </Button>
      </div>
      {isAlterDateAndDestinationModalOpen && (
        <AlterDateAndDestinationModal
          closeAlterDateAndDestinationModal={closeAlterDateAndDestionationModal}
        />
      )}
    </div>
  );
}
