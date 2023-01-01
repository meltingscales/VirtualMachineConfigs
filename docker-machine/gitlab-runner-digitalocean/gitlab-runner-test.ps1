# From https://testdriven.io/blog/gitlab-ci-docker/

# Note: Make sure to set $env:DIGITAL_OCEAN_ACCESS_TOKEN
# ex: $env:DIGITAL_OCEAN_ACCESS_TOKEN='12134121231'
docker-machine create `
    --driver digitalocean `
    --digitalocean-access-token $env:DIGITAL_OCEAN_ACCESS_TOKEN `
    --digitalocean-region "nyc1" `
    --digitalocean-image "debian-10-x64" `
    --digitalocean-size "s-4vcpu-8gb" `
    --engine-install-url "https://releases.rancher.com/install-docker/19.03.9.sh" `
    runner-node


# Note - you must add your public key using DigitalOcean's web interface here.
# https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/
# ex:
# ssh-keygen
# cat ~/.ssh/id_rsa.pub
# <put it into DigitalOcean>
docker-machine scp -r ./gitlab-runner-files/ root@runner-node:~/gitlab-runner-files